from datetime import datetime, timedelta


def esta_en_ventana_de_reserva(inicio: datetime, ahora: datetime) -> bool:
    return inicio - ahora <= timedelta(hours=24)
