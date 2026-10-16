from collections.abc import Mapping
from datetime import datetime

from ecoharmony.actividades import capacidad_actividad


def consultar_disponibilidad(
    actividad: str,
    inicio: datetime,
    ocupacion: Mapping[tuple[str, datetime], int],
) -> int:
    capacidad = capacidad_actividad(actividad)
    ocupados = ocupacion.get((actividad, inicio), 0)

    return capacidad - ocupados