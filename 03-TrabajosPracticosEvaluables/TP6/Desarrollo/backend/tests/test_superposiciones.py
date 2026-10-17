

from datetime import datetime, timedelta, timezone

from ecoharmony.inscripciones import Inscripcion
from ecoharmony.models.visitante import Visitante
from ecoharmony.superposiciones import tiene_superposicion

ZONA_ARGENTINA = timezone(timedelta(hours=-3))
MARTES_10 = datetime(2026, 10, 20, 10, 0, tzinfo=ZONA_ARGENTINA)


def test_sup_01_persona_sin_inscripciones_previas_no_tiene_superposicion():
    """SUP-01: sin inscripciones anteriores no existe superposición."""
    assert tiene_superposicion("12345678", MARTES_10, []) is False



def test_sup_02_misma_persona_con_otra_actividad_al_mismo_horario_tiene_superposicion():
    """SUP-02: el mismo DNI ya está inscripto en Safari a las 10:00."""
    existentes = [
        Inscripcion(
            actividad="Safari",
            inicio=MARTES_10,
            visitantes=[Visitante(nombre="Ana García", dni="12345678", edad=20)],
        )
    ]

    assert tiene_superposicion("12345678", MARTES_10, existentes) is True