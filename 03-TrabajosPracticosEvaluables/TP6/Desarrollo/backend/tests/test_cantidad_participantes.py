from ecoharmony.cantidad_participantes import (
    cantidad_valida,
    cantidad_coincide_con_visitantes,
)
from ecoharmony.models.visitante import Visitante



def test_can_01_rechaza_cero_participantes():
    resultado = cantidad_valida(0)

    assert resultado is False

def test_can_02_rechaza_cantidad_negativa():
    resultado = cantidad_valida(-1)

    assert resultado is False

def test_can_03_rechaza_cantidad_decimal():
    resultado = cantidad_valida(1.5)

    assert resultado is False

def test_can_04_rechaza_cantidad_incompatible_con_visitantes():
    visitantes = [
        Visitante(nombre="Ana Pérez", dni="30123456", edad=25),
        Visitante(nombre="Luis López", dni="12345678", edad=30),
    ]

    resultado = cantidad_coincide_con_visitantes(3, visitantes)

    assert resultado is False