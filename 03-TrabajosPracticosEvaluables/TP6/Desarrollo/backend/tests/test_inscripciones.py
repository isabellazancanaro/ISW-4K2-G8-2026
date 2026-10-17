
from datetime import datetime, timedelta, timezone

from ecoharmony.models.visitante import Visitante
from ecoharmony.inscripciones import ServicioInscripciones


def test_cup_01_registra_una_persona_con_cupos_disponibles():
    """CUP-01: registra una inscripción válida cuando hay cupos."""

    zona_argentina = timezone(timedelta(hours=-3))
    inicio = datetime(2026, 10, 20, 10, 0, tzinfo=zona_argentina)
    ahora = datetime(2026, 10, 19, 12, 0, tzinfo=zona_argentina)

    visitante = Visitante(
        nombre="Ana García",
        dni="12345678",
        edad=20,
        talle="M",
    )

    servicio = ServicioInscripciones()

    resultado = servicio.inscribir(
        actividad="Tirolesa",
        inicio=inicio,
        ahora=ahora,
        cantidad=1,
        visitantes=[visitante],
        actividad_terminos="Tirolesa",
        acepto_terminos=True,
    )

    assert resultado is not None
    assert resultado.actividad == "Tirolesa"
    assert resultado.inicio == inicio
    assert resultado.visitantes == [visitante]

def test_cup_01_conserva_inscripcion_registrada():
    """CUP-01: la inscripción confirmada queda registrada."""

    zona = timezone(timedelta(hours=-3))
    inicio = datetime(2026, 10, 20, 10, 0, tzinfo=zona)
    ahora = datetime(2026, 10, 19, 12, 0, tzinfo=zona)

    visitante = Visitante(
        nombre="Ana García",
        dni="12345678",
        edad=20,
        talle="M",
    )

    servicio = ServicioInscripciones()

    resultado = servicio.inscribir(
        actividad="Tirolesa",
        inicio=inicio,
        ahora=ahora,
        cantidad=1,
        visitantes=[visitante],
        actividad_terminos="Tirolesa",
        acepto_terminos=True,
    )

    assert len(servicio.inscripciones) == 1
    assert servicio.inscripciones[0] == resultado

def test_cup_02_ocupa_el_ultimo_cupo_disponible():
    """CUP-02: permite ocupar el último cupo disponible."""

    zona = timezone(timedelta(hours=-3))
    inicio = datetime(2026, 10, 20, 10, 0, tzinfo=zona)
    ahora = datetime(2026, 10, 19, 12, 0, tzinfo=zona)

    visitante = Visitante(
        nombre="Ana García",
        dni="12345678",
        edad=20,
        talle="M",
    )

    servicio = ServicioInscripciones()

    # Tirolesa tiene capacidad 10.
    # Simulamos que ya hay 9 lugares ocupados.
    servicio.ocupacion[("Tirolesa", inicio)] = 9

    resultado = servicio.inscribir(
        actividad="Tirolesa",
        inicio=inicio,
        ahora=ahora,
        cantidad=1,
        visitantes=[visitante],
        actividad_terminos="Tirolesa",
        acepto_terminos=True,
    )

    assert resultado is not None
    assert servicio.ocupacion[("Tirolesa", inicio)] == 10
    assert servicio.consultar_cupos("Tirolesa", inicio) == 0
