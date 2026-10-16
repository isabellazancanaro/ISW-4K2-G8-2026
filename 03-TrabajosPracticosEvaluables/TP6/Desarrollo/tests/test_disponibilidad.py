from ecoharmony.actividades import capacidad_actividad

from datetime import datetime, timedelta, timezone

from ecoharmony.disponibilidad import consultar_disponibilidad


def test_disp_01_capacidades_de_actividades():
    assert capacidad_actividad("Tirolesa") == 10
    assert capacidad_actividad("Safari") == 8
    assert capacidad_actividad("Palestra") == 12
    assert capacidad_actividad("Jardinería") == 12

def test_disp_02_disponibilidad_con_un_cupo_restante():
    zona_horaria = timezone(timedelta(hours=-3))
    inicio = datetime(2026, 10, 20, 9, 0, tzinfo=zona_horaria)

    ocupacion = {
        ("Tirolesa", inicio): 9
    }

    disponibles = consultar_disponibilidad(
        "Tirolesa", inicio, ocupacion
    )

    assert disponibles == 1
    assert ocupacion[("Tirolesa", inicio)] == 9

def test_disp_03_actividad_completa():
    zona_horaria = timezone(timedelta(hours=-3))
    inicio = datetime(2026, 10, 20, 9, 0, tzinfo=zona_horaria)

    ocupacion = {
        ("Tirolesa", inicio): 10
    }

    disponibles = consultar_disponibilidad(
        "Tirolesa", inicio, ocupacion
    )

    assert disponibles == 0
    assert ocupacion[("Tirolesa", inicio)] == 10