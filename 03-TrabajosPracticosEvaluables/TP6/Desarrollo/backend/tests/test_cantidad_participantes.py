from ecoharmony.cantidad_participantes import cantidad_valida


def test_can_01_rechaza_cero_participantes():
    resultado = cantidad_valida(0)

    assert resultado is False

def test_can_02_rechaza_cantidad_negativa():
    resultado = cantidad_valida(-1)

    assert resultado is False