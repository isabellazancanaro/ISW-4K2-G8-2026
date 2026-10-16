from dataclasses import dataclass


@dataclass(frozen=True)
class Actividad:
    nombre: str
    capacidad_maxima: int
    edad_minima: int = 0
    requiere_talle: bool = False

    def admite_edad(self, edad: int) -> bool:
        return edad >= self.edad_minima
