from datetime import time


def es_horario_valido(hora: time | None) -> bool:
    return 9 <= hora.hour <= 17