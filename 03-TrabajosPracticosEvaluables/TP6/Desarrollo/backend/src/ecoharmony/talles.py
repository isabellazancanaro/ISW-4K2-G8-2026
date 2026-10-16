
def es_talle_valido_para_actividad(
    actividad: str,
    talle: str | None
) -> bool:
    return actividad == "Tirolesa" and talle == "XL"
