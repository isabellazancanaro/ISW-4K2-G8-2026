from datetime import date

def es_fecha_habilitada(fecha: date) -> bool:
    return fecha.weekday() != 0 # weekday() obtiene el dia de la semana de la fecha (Lunes = 0)