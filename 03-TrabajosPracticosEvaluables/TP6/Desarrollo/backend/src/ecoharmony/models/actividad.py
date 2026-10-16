from dataclasses import dataclass


@dataclass(frozen=True)
class Actividad:
    nombre: str
    capacidad_maxima: int