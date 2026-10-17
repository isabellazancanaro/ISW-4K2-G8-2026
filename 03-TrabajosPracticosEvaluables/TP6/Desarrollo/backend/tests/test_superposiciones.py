from datetime import datetime, timedelta, timezone

from ecoharmony.superposiciones import tiene_superposicion

ZONA_ARGENTINA = timezone(timedelta(hours=-3))
MARTES_10 = datetime(2026, 10, 20, 10, 0, tzinfo=ZONA_ARGENTINA)


def test_sup_01_persona_sin_inscripciones_previas_no_tiene_superposicion():
    """SUP-01: sin inscripciones anteriores no existe superposición."""
    assert tiene_superposicion("12345678", MARTES_10, []) is False