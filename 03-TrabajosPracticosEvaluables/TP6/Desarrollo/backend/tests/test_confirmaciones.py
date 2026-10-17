import io
from datetime import datetime, timedelta, timezone

import zxingcpp
from PIL import Image

from ecoharmony.confirmaciones import NotificadorSimulado, ServicioConfirmaciones
from ecoharmony.inscripciones import Inscripcion
from ecoharmony.models.visitante import Visitante

ZONA_ARGENTINA = timezone(timedelta(hours=-3))
MARTES_10 = datetime(2026, 10, 20, 10, 0, tzinfo=ZONA_ARGENTINA)
EMAIL_TITULAR = "titular@ecoharmony.test"


def test_mail_01_confirmacion_exitosa_solicita_un_correo():
    """MAIL-01: confirmar una inscripción válida solicita el envío del correo."""
    inscripcion = Inscripcion(
        actividad="Tirolesa",
        inicio=MARTES_10,
        visitantes=[Visitante(nombre="Ana García", dni="12345678", edad=20, talle="M")],
    )
    notificador = NotificadorSimulado()
    servicio = ServicioConfirmaciones(notificador)

    servicio.confirmar(inscripcion, EMAIL_TITULAR)

    assert len(notificador.enviados) == 1



def test_mail_02_correo_incluye_orden_actividad_horario_participante_y_qr():
    """MAIL-02: el correo contiene todos los datos de la inscripción confirmada."""
    visitante = Visitante(nombre="Ana García", dni="12345678", edad=20, talle="M")
    inscripcion = Inscripcion(actividad="Tirolesa", inicio=MARTES_10, visitantes=[visitante])
    notificador = NotificadorSimulado()
    servicio = ServicioConfirmaciones(notificador)

    servicio.confirmar(inscripcion, EMAIL_TITULAR)

    correo = notificador.enviados[0]
    assert correo.destinatario == EMAIL_TITULAR
    assert correo.numero_orden == "ORD-0001"
    assert correo.actividad == "Tirolesa"
    assert correo.inicio == MARTES_10
    assert len(correo.participantes) == 1

    participante = correo.participantes[0]
    assert participante.visitante == visitante
    assert "ORD-0001" in participante.codigo_qr
    assert "12345678" in participante.codigo_qr



def test_mail_03_grupo_de_tres_recibe_tres_participantes_con_qr_legibles():
    """MAIL-03: cada participante del grupo tiene su propio QR funcional."""
    visitantes = [
        Visitante(nombre="Ana García", dni="11111111", edad=20, talle="M"),
        Visitante(nombre="Bruno Díaz", dni="22222222", edad=25, talle="L"),
        Visitante(nombre="Carla Ruiz", dni="33333333", edad=30, talle="S"),
    ]
    inscripcion = Inscripcion(actividad="Tirolesa", inicio=MARTES_10, visitantes=visitantes)
    notificador = NotificadorSimulado()
    servicio = ServicioConfirmaciones(notificador)

    servicio.confirmar(inscripcion, EMAIL_TITULAR)

    participantes = notificador.enviados[0].participantes
    assert [p.visitante for p in participantes] == visitantes
    assert len({p.codigo_qr for p in participantes}) == 3

    for participante in participantes:
        leidos = zxingcpp.read_barcodes(Image.open(io.BytesIO(participante.imagen_qr)))
        assert [codigo.text for codigo in leidos] == [participante.codigo_qr]
        assert participante.visitante.dni in participante.codigo_qr