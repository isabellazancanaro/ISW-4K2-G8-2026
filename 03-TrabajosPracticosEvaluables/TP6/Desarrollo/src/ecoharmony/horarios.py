from datetime import time


def es_horario_valido(hora: time | None) -> bool:
    return (
        hora is not None
        and 9 <= hora.hour <= 17
        and hora.minute == 0
        and hora.second == 0
        and hora.microsecond == 0
    )