
from ecoharmony.models.visitante import Visitante


def cantidad_valida(cantidad: int | float) -> bool:
    return type(cantidad) is int and cantidad > 0


def cantidad_coincide_con_visitantes(
    cantidad: int,
    visitantes: list[Visitante],
) -> bool:
    return cantidad_valida(cantidad) and cantidad == len(visitantes)
