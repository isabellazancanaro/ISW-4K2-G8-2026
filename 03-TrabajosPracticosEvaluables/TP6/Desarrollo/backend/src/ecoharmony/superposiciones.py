from datetime import datetime, timedelta

from ecoharmony.inscripciones import Inscripcion
from ecoharmony.models.visitante import Visitante

DURACION_ACTIVIDAD = timedelta(hours=1)


def tiene_superposicion(
    dni: str,
    inicio: datetime,
    inscripciones_existentes: list[Inscripcion],
) -> bool:
    fin = inicio + DURACION_ACTIVIDAD

    for inscripcion in inscripciones_existentes:
        inscripto = any(v.dni == dni for v in inscripcion.visitantes)
        fin_existente = inscripcion.inicio + DURACION_ACTIVIDAD
        se_cruzan = inicio < fin_existente and inscripcion.inicio < fin

        if inscripto and se_cruzan:
            return True

    return False



def tiene_superposicion_grupo(
    visitantes: list[Visitante],
    inicio: datetime,
    inscripciones_existentes: list[Inscripcion],
) -> bool:
    return any(
        tiene_superposicion(visitante.dni, inicio, inscripciones_existentes)
        for visitante in visitantes
    )