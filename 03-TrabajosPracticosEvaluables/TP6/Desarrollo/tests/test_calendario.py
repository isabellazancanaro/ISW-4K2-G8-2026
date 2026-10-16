from datetime import date

from ecoharmony.calendario import es_fecha_habilitada


def test_fec_01_dia_habilitado():
    fecha = date(2026, 10, 20)

    resultado = es_fecha_habilitada(fecha)

    assert resultado is True


def test_fec_02_parque_cerrado_lunes():
    fecha = date(2026, 10, 19)

    resultado = es_fecha_habilitada(fecha)

    assert resultado is False
    

def test_fec_03_cierre_25_diciembre():
    fecha = date(2026, 12, 25)

    resultado = es_fecha_habilitada(fecha)

    assert resultado is False