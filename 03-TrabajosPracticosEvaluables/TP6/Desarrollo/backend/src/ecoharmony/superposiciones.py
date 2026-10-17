from datetime import datetime, timedelta

from ecoharmony.inscripciones import Inscripcion

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