
from ecoharmony.talles import es_talle_valido_para_actividad


def test_tal_01_tirolesa_acepta_talle_xl():
    resultado = es_talle_valido_para_actividad("Tirolesa", "XL")

    assert resultado is True
