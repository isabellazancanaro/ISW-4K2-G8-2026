from datetime import date


def es_fecha_habilitada(fecha: date) -> bool:
    return fecha.weekday() != 0 and (fecha.month, fecha.day) != (12, 25)