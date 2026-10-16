from ecoharmony.models.actividad import Actividad


ACTIVIDADES: dict[str, Actividad] = {
    actividad.nombre: actividad
    for actividad in (
        Actividad("Tirolesa", 10),
        Actividad("Safari", 8),
        Actividad("Palestra", 12),
        Actividad("Jardinería", 12),
    )
}


def es_actividad_valida(nombre: str) -> bool:
    return nombre in ACTIVIDADES


def capacidad_actividad(nombre: str) -> int:
    return ACTIVIDADES[nombre].capacidad_maxima