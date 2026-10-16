
def es_aceptacion_terminos_valida(
    actividad: str,
    actividad_terminos: str | None,
    acepto: bool | None
) -> bool:
    return (
        actividad == "Tirolesa"
        and actividad_terminos == "Tirolesa"
        and acepto is True
    )
