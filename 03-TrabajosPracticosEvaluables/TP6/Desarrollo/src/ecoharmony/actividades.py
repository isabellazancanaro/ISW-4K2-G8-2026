ACTIVIDADES = {
    "Tirolesa": 10,
    "Safari": 8,
    "Palestra": 12,
    "Jardinería": 12,
}


def es_actividad_valida(nombre: str) -> bool:
    return nombre in ACTIVIDADES


def capacidad_actividad(nombre: str) -> int:
    return ACTIVIDADES[nombre]