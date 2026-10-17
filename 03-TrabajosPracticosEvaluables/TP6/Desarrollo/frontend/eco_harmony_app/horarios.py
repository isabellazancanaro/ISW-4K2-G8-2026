"""Opciones de calendario para las vistas, usando las reglas del dominio."""

from datetime import date, datetime, time, timedelta

from ecoharmony.anticipacion import esta_en_ventana_de_reserva
from ecoharmony.calendario import es_fecha_habilitada
from ecoharmony.horarios import es_horario_valido

DIAS = ("lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo")


def horas_inscribibles(dia: date, ahora: datetime):
    if not es_fecha_habilitada(dia):
        return []
    turnos = []
    for hora in range(24):
        turno = datetime.combine(dia, time(hora), tzinfo=ahora.tzinfo)
        if es_horario_valido(turno.time()) and esta_en_ventana_de_reserva(turno, ahora):
            turnos.append(turno)
    return turnos


def dias_inscribibles(ahora: datetime):
    dias = []
    for desplazamiento, prefijo in ((0, "Hoy"), (1, "Mañana")):
        dia = ahora.date() + timedelta(days=desplazamiento)
        if horas_inscribibles(dia, ahora):
            dias.append((dia.isoformat(), f"{prefijo} · {DIAS[dia.weekday()]} {dia:%d/%m}"))
    return dias
