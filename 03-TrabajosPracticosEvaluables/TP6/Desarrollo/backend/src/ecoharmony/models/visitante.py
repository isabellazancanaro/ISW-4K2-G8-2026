from dataclasses import dataclass


@dataclass(frozen=True)
class Visitante:
    nombre: str | None
    dni: str | None
    edad: int | None
    talle: str | None = None