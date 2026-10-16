from ecoharmony.edades import es_edad_valida_para_actividad


def test_ed_02_palestra_acepta_edad_minima():
    resultado = es_edad_valida_para_actividad("Palestra", 12)

    assert resultado is True


def test_ed_01_palestra_rechaza_menor_de_12():
    resultado = es_edad_valida_para_actividad("Palestra", 11)

    assert resultado is False


def test_ed_03_tirolesa_rechaza_menor_de_8():
    resultado = es_edad_valida_para_actividad("Tirolesa", 7)

    assert resultado is False


def test_ed_04_tirolesa_acepta_edad_minima():
    resultado = es_edad_valida_para_actividad("Tirolesa", 8)

    assert resultado is True


def test_ed_05_safari_acepta_visitante_de_un_ano():
    resultado = es_edad_valida_para_actividad("Safari", 1)

    assert resultado is True


def test_ed_06_jardineria_acepta_visitante_de_un_ano():
    resultado = es_edad_valida_para_actividad("Jardinería", 1)

    assert resultado is True


def test_ed_11_safari_acepta_edad_cero():
    resultado = es_edad_valida_para_actividad("Safari", 0)

    assert resultado is True


def test_ed_07_safari_acepta_visitante_de_90_anos():
    resultado = es_edad_valida_para_actividad("Safari", 90)

    assert resultado is True


def test_ed_07_jardineria_acepta_visitante_de_90_anos():
    resultado = es_edad_valida_para_actividad("Jardinería", 90)

    assert resultado is True


def test_ed_08_rechaza_edad_omitida():
    resultado = es_edad_valida_para_actividad("Safari", None)

    assert resultado is False


