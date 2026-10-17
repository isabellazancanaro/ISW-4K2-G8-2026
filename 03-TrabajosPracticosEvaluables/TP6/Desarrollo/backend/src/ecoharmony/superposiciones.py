from datetime import datetime

from ecoharmony.inscripciones import Inscripcion


def tiene_superposicion(
    dni: str,
    inicio: datetime,
    inscripciones_existentes: list[Inscripcion],
) -> bool:
    return False