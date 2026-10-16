from ecoharmony.datos_visitante import (
    identificacion_visitante_valida,
    identificaciones_grupo_validas,
)
from ecoharmony.models.visitante import Visitante


def test_dat_01_dni_informado_correctamente():
    visitante = Visitante(
        nombre="Ana Pérez",
        dni="30123456",
        edad=25,
    )

    resultado = identificacion_visitante_valida(visitante)

    assert resultado is True

def test_dat_02_rechaza_dni_omitido():
    visitante = Visitante(
        nombre="Ana Pérez",
        dni=None,
        edad=25,
    )

    resultado = identificacion_visitante_valida(visitante)

    assert resultado is False

def test_dat_03_rechaza_nombre_omitido():
    visitante = Visitante(
        nombre=None,
        dni="30123456",
        edad=25,
    )

    resultado = identificacion_visitante_valida(visitante)

    assert resultado is False

def test_dat_04_rechaza_dni_con_letras():
    visitante = Visitante(
        nombre="Ana Pérez",
        dni="ABC12345",
        edad=25,
    )

    resultado = identificacion_visitante_valida(visitante)

    assert resultado is False

def test_dat_05_rechaza_grupo_con_persona_incompleta():
    visitantes = [
        Visitante(nombre="Ana Pérez", dni="30123456", edad=25),
        Visitante(nombre="Luis López", dni="1234567", edad=30),
        Visitante(nombre="María Díaz", dni=None, edad=20),
    ]

    resultado = identificaciones_grupo_validas(visitantes)

    assert resultado is False

def test_dat_06_acepta_dni_de_siete_digitos():
    visitante = Visitante(
        nombre="Ana Pérez",
        dni="1234567",
        edad=25,
    )

    resultado = identificacion_visitante_valida(visitante)

    assert resultado is True

def test_dat_07_rechaza_dni_de_seis_digitos():
    visitante = Visitante(
        nombre="Ana Pérez",
        dni="123456",
        edad=25,
    )

    resultado = identificacion_visitante_valida(visitante)

    assert resultado is False