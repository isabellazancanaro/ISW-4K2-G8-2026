from ecoharmony.models.visitante import Visitante


def identificacion_visitante_valida(visitante: Visitante) -> bool:
    return (
        bool(visitante.nombre and visitante.nombre.strip())
        and visitante.dni is not None
        and visitante.dni.isdigit()
        and 7 <= len(visitante.dni) <= 8
    )

def identificaciones_grupo_validas(visitantes: list[Visitante]) -> bool:
    return all(
        identificacion_visitante_valida(visitante)
        for visitante in visitantes
    )