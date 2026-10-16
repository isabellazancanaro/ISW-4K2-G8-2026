
TALLES_VALIDOS = {"XS", "S", "M", "L", "XL", "XXL"}


def es_talle_valido_para_actividad(
    actividad: str,
    talle: str | None
) -> bool:
    return (
        (actividad in ("Tirolesa", "Palestra") and talle in TALLES_VALIDOS)
        or (actividad in ("Safari", "Jardinería") and talle is None)
    )
