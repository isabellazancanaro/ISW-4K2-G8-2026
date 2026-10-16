from ecoharmony.models.visitante import Visitante


def identificacion_visitante_valida(visitante: Visitante) -> bool:
    return visitante.dni is not None