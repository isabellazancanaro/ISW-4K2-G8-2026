from datetime import datetime, timedelta


def esta_en_ventana_de_reserva(inicio: datetime, ahora: datetime) -> bool:
    return timedelta(minutes=15) <= inicio - ahora <= timedelta(hours=24)