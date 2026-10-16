def cantidad_valida(cantidad: int | float) -> bool:
    return type(cantidad) is int and cantidad > 0