def es_edad_valida_para_actividad(actividad: str, edad: int | None) -> bool:
    if edad is None or edad < 0:
        return False

    if actividad == "Palestra":
        return edad >= 12

    if actividad == "Tirolesa":
        return edad >= 8

    return True
