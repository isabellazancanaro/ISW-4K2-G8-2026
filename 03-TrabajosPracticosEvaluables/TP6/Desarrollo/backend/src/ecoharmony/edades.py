
def es_edad_valida_para_actividad(actividad: str, edad: int) -> bool:
    if actividad == "Palestra":
        return edad >= 12

    return True
