from ecoharmony.edades import es_edad_valida_para_actividad


def test_ed_02_palestra_acepta_edad_minima():
    resultado = es_edad_valida_para_actividad("Palestra", 12)

    assert resultado is True


def test_ed_01_palestra_rechaza_menor_de_12():
    resultado = es_edad_valida_para_actividad("Palestra", 11)

    assert resultado is False
