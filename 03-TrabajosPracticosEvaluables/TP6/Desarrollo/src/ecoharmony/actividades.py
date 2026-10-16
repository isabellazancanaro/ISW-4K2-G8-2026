ACTIVIDADES_VALIDAS = ("Tirolesa", "Safari", "Palestra", "Jardinería")

CAPACIDADES_POR_ACTIVIDAD = {
    "Tirolesa": 10,
    "Safari": 8,
    "Palestra": 12,
    "Jardinería": 12,
}


def es_actividad_valida(nombre: str) -> bool:
    return nombre in ACTIVIDADES_VALIDAS


def capacidad_actividad(nombre: str) -> int:
    return CAPACIDADES_POR_ACTIVIDAD[nombre]