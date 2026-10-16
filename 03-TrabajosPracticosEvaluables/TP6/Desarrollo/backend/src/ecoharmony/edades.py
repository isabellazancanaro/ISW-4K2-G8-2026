def es_edad_valida_para_actividad(actividad: str, edad: int | None) -> bool:
    if type(edad) is not int or edad < 0:
        return False

    if actividad == "Palestra":
        return edad >= 12

    if actividad == "Tirolesa":
        return edad >= 8

    return True
