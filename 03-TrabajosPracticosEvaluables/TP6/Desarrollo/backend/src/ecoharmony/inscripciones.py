
from dataclasses import dataclass
from datetime import datetime
from ecoharmony.disponibilidad import consultar_disponibilidad
from ecoharmony.models.visitante import Visitante


@dataclass(frozen=True)
class Inscripcion:
    actividad: str
    inicio: datetime
    visitantes: list[Visitante]


class ServicioInscripciones:

    def __init__(self):
        self._inscripciones: list[Inscripcion] = []
        self.ocupacion: dict[tuple[str, datetime], int] = {}

    @property
    def inscripciones(self) -> tuple[Inscripcion, ...]:
        return tuple(self._inscripciones)

    def consultar_cupos(
        self,
        actividad: str,
        inicio: datetime,
    ) -> int:
        return consultar_disponibilidad(
            actividad,
            inicio,
            self.ocupacion,
        )

    def inscribir(
        self,
        actividad: str,
        inicio: datetime,
        ahora: datetime,
        cantidad: int,
        visitantes: list[Visitante],
        actividad_terminos: str,
        acepto_terminos: bool,
    ) -> Inscripcion:

        inscripcion = Inscripcion(
            actividad=actividad,
            inicio=inicio,
            visitantes=list(visitantes),
        )

        self._inscripciones.append(inscripcion)
        
        clave = (actividad, inicio)

        self.ocupacion[clave] = (
            self.ocupacion.get(clave, 0) + cantidad
        )

        return inscripcion
