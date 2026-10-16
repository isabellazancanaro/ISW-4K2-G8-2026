from ecoharmony.cantidad_participantes import cantidad_valida


def test_can_01_rechaza_cero_participantes():
    resultado = cantidad_valida(0)

    assert resultado is False