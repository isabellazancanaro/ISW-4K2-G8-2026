ACTIVIDADES_VALIDAS = ("Tirolesa", "Safari", "Palestra", "Jardinería")


def es_actividad_valida(nombre: str) -> bool:
    return nombre in ACTIVIDADES_VALIDAS