
ACTIVIDADES_VALIDAS = {
    "Tirolesa",
    "Safari",
    "Palestra",
    "Jardinería",
}


def es_aceptacion_terminos_valida(
    actividad: str,
    actividad_terminos: str | None,
    acepto: bool | None
) -> bool:
    return (
        actividad in ACTIVIDADES_VALIDAS
        and actividad_terminos == actividad
        and acepto is True
    )
