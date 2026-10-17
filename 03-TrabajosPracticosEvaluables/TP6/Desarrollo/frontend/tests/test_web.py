import base64
from contextlib import contextmanager
from datetime import datetime, timedelta, timezone
from io import BytesIO

import pytest
import zxingcpp
from flask import template_rendered
from PIL import Image
from werkzeug.datastructures import MultiDict

from frontend.eco_harmony_app.app import crear_app


ZONA = timezone(timedelta(hours=-3))
AHORA = datetime(2026, 10, 20, 9, tzinfo=ZONA)


@pytest.fixture
def app():
    return crear_app({"TESTING": True, "RELOJ": lambda: AHORA})


@contextmanager
def plantillas(app):
    contextos = []

    def capturar(sender, template, context, **extra):
        contextos.append(context)

    with template_rendered.connected_to(capturar, app):
        yield contextos


def solicitud(actividad="Tirolesa", turno="2026-10-20T10:00", dnis=("01234567",)):
    datos = MultiDict({
        "actividad": actividad, "turno": turno, "cantidad": str(len(dnis)),
        "email": "titular@example.com", "terminos": "1",
    })
    for dni in dnis:
        datos.add("nombre", "Ana García")
        datos.add("dni", dni)
        datos.add("edad", "20")
        if actividad in ("Tirolesa", "Palestra"):
            datos.add("talle", "M")
    return datos


def sin_efectos(app):
    estado = app.extensions["ecoharmony"]
    assert estado["servicio"].inscripciones == ()
    assert estado["servicio"].ocupacion == {}
    assert estado["notificador"].enviados == []
    assert estado["confirmaciones"] == {}


def test_inscripcion_grupal_confirmacion_y_qr_reales(app):
    cliente = app.test_client()
    with plantillas(app) as contextos:
        respuesta = cliente.post("/inscripcion", data=solicitud(dnis=("01234567", "12345678")), follow_redirects=True)
    assert respuesta.status_code == 200
    html = respuesta.get_data(as_text=True)
    assert 'class="codigo-qr" src="data:image/png;base64,' in html
    assert "ORD-0001" in html
    assert "Confirmación por correo (simulada)" in html
    assert "Esta demostración no envía emails reales" in html
    contexto = contextos[-1]
    assert contexto["inscripcion"]["numero_orden"] == "ORD-0001"
    assert contexto["inscripcion"]["email"] == "titular@example.com"
    assert contexto["visitantes"][0]["dni"] == "01234567"
    assert len(contexto["visitantes"]) == 2
    for visitante in contexto["visitantes"]:
        png = base64.b64decode(visitante["qr_data_uri"].split(",", 1)[1])
        qr = zxingcpp.read_barcode(Image.open(BytesIO(png)))
        assert qr.text == visitante["codigo_qr"]
    enviados = app.extensions["ecoharmony"]["notificador"].enviados
    assert len(enviados) == 1
    assert enviados[0] is contexto["correo"]


@pytest.mark.parametrize("campo,valor", [
    ("turno", "invalido"), ("cantidad", "1.5"), ("cantidad", ""),
    ("edad", "20.5"), ("email", ""), ("email", "sin-arroba"),
])
def test_datos_http_mal_formados_no_registran(app, campo, valor):
    datos = solicitud()
    datos[campo] = valor
    with plantillas(app) as contextos:
        respuesta = app.test_client().post("/inscripcion", data=datos)
    assert respuesta.status_code == 400
    assert 'role="alert"' in respuesta.get_data(as_text=True)
    assert contextos[-1]["error"]
    assert contextos[-1]["valores"][campo] == [valor]
    sin_efectos(app)


@pytest.mark.parametrize("campo,valor", [
    ("actividad", "Desconocida"), ("edad", "7"), ("nombre", ""),
    ("talle", "INVALIDO"), ("terminos", ""), ("cantidad", "2"),
    ("turno", "2026-10-20T18:00"), ("turno", "2026-10-19T10:00"),
])
def test_rechazo_del_dominio_sin_efectos(app, campo, valor):
    datos = solicitud()
    datos[campo] = valor
    with plantillas(app) as contextos:
        respuesta = app.test_client().post("/inscripcion", data=datos)
    assert respuesta.status_code == 422
    assert "No se pudo confirmar" in respuesta.get_data(as_text=True)
    assert "No se pudo confirmar" in contextos[-1]["error"]
    sin_efectos(app)


def test_listas_desalineadas_no_registran(app):
    datos = solicitud(dnis=("01234567", "12345678"))
    datos.setlist("edad", ["20"])
    assert app.test_client().post("/inscripcion", data=datos).status_code == 400
    sin_efectos(app)


def test_safari_rechaza_talle_adicional(app):
    datos = solicitud(actividad="Safari")
    datos["talle"] = "M"
    assert app.test_client().post("/inscripcion", data=datos).status_code == 422
    sin_efectos(app)


def test_reservas_consecutivas_cupos_y_superposicion(app):
    cliente = app.test_client()
    assert cliente.post("/inscripcion", data=solicitud()).status_code == 302
    assert cliente.post("/inscripcion", data=solicitud(dnis=("12345678",))).status_code == 302
    horarios = cliente.get("/api/horarios?actividad=Tirolesa&fecha=2026-10-20").json
    assert next(h for h in horarios if h["texto"] == "10:00")["disponibles"] == 8
    estado = app.extensions["ecoharmony"]
    assert cliente.post("/inscripcion", data=solicitud(actividad="Safari")).status_code == 422
    assert len(estado["servicio"].inscripciones) == 2
    assert len(estado["notificador"].enviados) == 2
    assert cliente.post("/inscripcion", data=solicitud(turno="2026-10-20T11:00")).status_code == 302


def test_cupo_agotado_rechaza_grupo_sin_correo(app):
    cliente = app.test_client()
    dnis = tuple(str(20000000 + n) for n in range(10))
    assert cliente.post("/inscripcion", data=solicitud(dnis=dnis)).status_code == 302
    assert cliente.post("/inscripcion", data=solicitud()).status_code == 422
    estado = app.extensions["ecoharmony"]
    assert len(estado["servicio"].inscripciones) == 1
    assert len(estado["notificador"].enviados) == 1


def test_horarios_limites_cierres_y_reloj_no_controlado_por_url(app):
    cliente = app.test_client()
    horarios = cliente.get("/api/horarios?actividad=Safari&fecha=2026-10-20&ahora=2030-01-01T00:00").json
    assert [h["texto"] for h in horarios] == [f"{h:02}:00" for h in range(10, 18)]
    assert cliente.get("/api/horarios?actividad=Safari&fecha=2026-10-19").json == []
    assert cliente.get("/api/horarios?actividad=Safari&fecha=2026-10-22").json == []
    assert cliente.get("/api/horarios?actividad=Safari&fecha=mal").status_code == 400
    assert cliente.get("/api/horarios?actividad=Otro&fecha=2026-10-20").status_code == 404
    assert cliente.get("/inscripcion/999").status_code == 404


def test_fallo_confirmacion_revierte_y_no_muestra_exito(app, monkeypatch):
    def fallar(*args):
        raise RuntimeError("fallo simulado")

    monkeypatch.setattr(app.extensions["ecoharmony"]["notificador"], "enviar", fallar)
    assert app.test_client().post("/inscripcion", data=solicitud()).status_code == 503
    sin_efectos(app)


def test_instancias_independientes_y_turno_con_offset(app):
    cliente = app.test_client()
    assert cliente.post("/inscripcion", data=solicitud(turno="2026-10-20T13:00+00:00")).status_code == 302
    otra_app = crear_app({"TESTING": True, "RELOJ": lambda: AHORA})
    sin_efectos(otra_app)


@pytest.mark.parametrize("minutos", [15, 24 * 60])
def test_limites_inclusivos_en_consulta_y_registro(app, minutos):
    turno = datetime(2026, 10, 20, 10, tzinfo=ZONA)
    app.config["RELOJ"] = lambda: turno - timedelta(minutes=minutos)
    cliente = app.test_client()
    horarios = cliente.get("/api/horarios?actividad=Safari&fecha=2026-10-20").json
    assert any(h["texto"] == "10:00" for h in horarios)
    assert cliente.post("/inscripcion", data=solicitud(actividad="Safari")).status_code == 302


def test_grupo_con_un_visitante_invalido_no_registra_a_nadie(app):
    datos = solicitud(dnis=("01234567", "12345678"))
    datos.setlist("edad", ["20", "7"])
    assert app.test_client().post("/inscripcion", data=datos).status_code == 422
    sin_efectos(app)


def test_cantidad_superior_al_cupo_rechazada_desde_http(app):
    dnis = tuple(str(20000000 + n) for n in range(11))
    respuesta = app.test_client().post("/inscripcion", data=solicitud(dnis=dnis))
    assert respuesta.status_code == 422
    assert "No se pudo confirmar" in respuesta.get_data(as_text=True)
    sin_efectos(app)
