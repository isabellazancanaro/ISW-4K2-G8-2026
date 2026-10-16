from ecoharmony.actividades import ACTIVIDADES


TALLES_VALIDOS = {"XS", "S", "M", "L", "XL", "XXL"}


def es_talle_valido_para_actividad(
    actividad: str,
    talle: str | None,
) -> bool:
    actividad_objeto = ACTIVIDADES.get(actividad)

    if actividad_objeto is None:
        return False

    if actividad_objeto.requiere_talle:
        return talle in TALLES_VALIDOS

    return talle is None
