from ecoharmony.actividades import es_actividad_valida


def es_aceptacion_terminos_valida(
    actividad: str,
    actividad_terminos: str | None,
    acepto: bool | None,
) -> bool:
    return (
        es_actividad_valida(actividad)
        and actividad_terminos == actividad
        and acepto is True
    )
