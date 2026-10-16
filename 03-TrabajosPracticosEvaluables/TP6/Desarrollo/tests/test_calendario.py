from datetime import date

from ecoharmony.calendario import es_fecha_habilitada


def test_fec_01_dia_habilitado():
    fecha = date(2026, 10, 20)

    resultado = es_fecha_habilitada(fecha)

    assert resultado is True