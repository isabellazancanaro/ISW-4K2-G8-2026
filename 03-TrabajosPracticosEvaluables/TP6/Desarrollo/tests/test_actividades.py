from ecoharmony.actividades import es_actividad_valida


def test_act_01_tirolesa_es_actividad_valida():
    assert es_actividad_valida("Tirolesa") is True