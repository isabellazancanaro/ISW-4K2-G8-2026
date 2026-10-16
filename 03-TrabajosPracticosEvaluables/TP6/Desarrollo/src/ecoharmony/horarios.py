from datetime import time


def es_horario_valido(hora: time | None) -> bool:
    return hora.hour >= 9