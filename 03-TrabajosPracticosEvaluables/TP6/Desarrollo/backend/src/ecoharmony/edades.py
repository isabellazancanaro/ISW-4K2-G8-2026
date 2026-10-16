def es_edad_valida_para_actividad(actividad: str, edad: int) -> bool:
    if actividad == "Palestra":
        return edad >= 12

    if actividad == "Tirolesa":
        return edad >= 8

    return True
