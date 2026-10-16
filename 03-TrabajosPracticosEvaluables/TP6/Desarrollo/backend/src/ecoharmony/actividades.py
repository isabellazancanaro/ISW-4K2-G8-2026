from ecoharmony.models.actividad import Actividad


ACTIVIDADES: dict[str, Actividad] = {
    actividad.nombre: actividad
    for actividad in (
        Actividad(
            nombre="Tirolesa",
            capacidad_maxima=10,
            edad_minima=8,
            requiere_talle=True,
        ),
        Actividad(
            nombre="Safari",
            capacidad_maxima=8,
            edad_minima=0,
            requiere_talle=False,
        ),
        Actividad(
            nombre="Palestra",
            capacidad_maxima=12,
            edad_minima=12,
            requiere_talle=True,
        ),
        Actividad(
            nombre="Jardinería",
            capacidad_maxima=12,
            edad_minima=0,
            requiere_talle=False,
        ),
    )
}


def es_actividad_valida(nombre: str) -> bool:
    return nombre in ACTIVIDADES


def capacidad_actividad(nombre: str) -> int:
    return ACTIVIDADES[nombre].capacidad_maxima
