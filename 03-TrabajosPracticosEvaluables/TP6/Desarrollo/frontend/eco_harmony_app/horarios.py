from datetime import date, datetime, time, timedelta

HORAS = range(9, 18)  # 9:00 a 17:00; a las 18:00 no hay turno
FERIADOS = {(12, 25), (1, 1)}  # (mes, día)
ANTICIPACION_MAXIMA = timedelta(hours=24)
CIERRE_INSCRIPCION = timedelta(minutes=15)

DIAS = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]


def parque_abierto(dia: date) -> bool:
    return dia.weekday() != 0 and (dia.month, dia.day) not in FERIADOS  # 0 = lunes


def error_de_ventana(turno: datetime, ahora: datetime):
    """None si se puede inscribir; si no, qué regla incumple."""
    anticipacion = turno - ahora
    if anticipacion > ANTICIPACION_MAXIMA:
        return "ANTICIPACION_EXCEDIDA"
    if anticipacion < CIERRE_INSCRIPCION:
        return "INSCRIPCION_CERRADA"
    return None


def horas_inscribibles(dia: date, ahora: datetime):
    """Turnos (datetime) de ese día que todavía se pueden reservar."""
    if not parque_abierto(dia):
        return []
    turnos = []
    for hora in HORAS:
        turno = datetime.combine(dia, time(hora))
        if error_de_ventana(turno, ahora) is None:
            turnos.append(turno)
    return turnos


def dias_inscribibles(ahora: datetime):
    """[(valor 'YYYY-MM-DD', etiqueta)] de hoy y mañana, solo si tienen algún turno."""
    dias = []
    for desplazamiento, prefijo in ((0, "Hoy"), (1, "Mañana")):
        dia = ahora.date() + timedelta(days=desplazamiento)
        if horas_inscribibles(dia, ahora):
            dias.append((dia.isoformat(), f"{prefijo} · {DIAS[dia.weekday()]} {dia:%d/%m}"))
    return dias