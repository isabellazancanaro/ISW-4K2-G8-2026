
from dataclasses import dataclass
from datetime import datetime

from ecoharmony.models.visitante import Visitante


@dataclass(frozen=True)
class Inscripcion:
    actividad: str
    inicio: datetime
    visitantes: list[Visitante]


class ServicioInscripciones:
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
        return Inscripcion(
            actividad=actividad,
            inicio=inicio,
            visitantes=visitantes,
        )
