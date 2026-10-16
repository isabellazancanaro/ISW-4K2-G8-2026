
from ecoharmony.talles import es_talle_valido_para_actividad


def test_tal_01_tirolesa_acepta_talle_xl():
    resultado = es_talle_valido_para_actividad("Tirolesa", "XL")

    assert resultado is True


def test_tal_02_palestra_acepta_talle_xl():
    resultado = es_talle_valido_para_actividad("Palestra", "XL")

    assert resultado is True


def test_tal_03_tirolesa_rechaza_talle_inexistente():
    resultado = es_talle_valido_para_actividad("Tirolesa", "XXXL")

    assert resultado is False



def test_tal_04_tirolesa_rechaza_talle_omitido():
    resultado = es_talle_valido_para_actividad("Tirolesa", None)

    assert resultado is False


def test_tal_05_palestra_rechaza_talle_omitido():
    resultado = es_talle_valido_para_actividad("Palestra", None)

    assert resultado is False
