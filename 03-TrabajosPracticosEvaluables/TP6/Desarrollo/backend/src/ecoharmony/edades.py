from ecoharmony.actividades import ACTIVIDADES


def es_edad_valida_para_actividad(actividad: str, edad: int | None) -> bool:
    if type(edad) is not int or edad < 0:
        return False

    actividad_objeto = ACTIVIDADES.get(actividad)

    if actividad_objeto is None:
        return True

    return actividad_objeto.admite_edad(edad)
