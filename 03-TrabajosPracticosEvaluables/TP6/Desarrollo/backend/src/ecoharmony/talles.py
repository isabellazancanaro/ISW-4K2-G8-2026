
def es_talle_valido_para_actividad(
    actividad: str,
    talle: str | None
) -> bool:
    return (
        (actividad in ("Tirolesa", "Palestra") and talle == "XL")
        or (actividad == "Safari" and talle is None)
    )
