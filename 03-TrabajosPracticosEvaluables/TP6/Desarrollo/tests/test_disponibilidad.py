from ecoharmony.actividades import capacidad_actividad


def test_disp_01_capacidades_de_actividades():
    assert capacidad_actividad("Tirolesa") == 10
    assert capacidad_actividad("Safari") == 8
    assert capacidad_actividad("Palestra") == 12
    assert capacidad_actividad("Jardinería") == 12