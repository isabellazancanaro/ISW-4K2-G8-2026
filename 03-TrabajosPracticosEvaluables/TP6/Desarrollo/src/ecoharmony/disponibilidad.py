from collections.abc import Mapping
from datetime import datetime


def consultar_disponibilidad(
    actividad: str,
    inicio: datetime,
    ocupacion: Mapping[tuple[str, datetime], int],
) -> int:
    return 0