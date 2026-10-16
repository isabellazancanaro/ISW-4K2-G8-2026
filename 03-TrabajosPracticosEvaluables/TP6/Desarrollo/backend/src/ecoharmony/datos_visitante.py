from ecoharmony.models.visitante import Visitante


def identificacion_visitante_valida(visitante: Visitante) -> bool:
    return (
        bool(visitante.nombre and visitante.nombre.strip())
        and visitante.dni is not None
        and visitante.dni.isdigit()
    )