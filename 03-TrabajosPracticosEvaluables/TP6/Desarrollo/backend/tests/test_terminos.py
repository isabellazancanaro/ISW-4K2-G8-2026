import pytest
from ecoharmony.terminos import es_aceptacion_terminos_valida


def test_tyc_01_aceptar_terminos_correctos_tirolesa():
    resultado = es_aceptacion_terminos_valida(
        "Tirolesa",
        "Tirolesa",
        True
    )

    assert resultado is True


def test_tyc_02_rechaza_terminos_no_aceptados():
    resultado = es_aceptacion_terminos_valida(
        "Tirolesa",
        "Tirolesa",
        False
    )

    assert resultado is False


@pytest.mark.parametrize(
    "actividad",
    ["Safari", "Palestra", "Jardinería"]
)
def test_tyc_03_aceptar_terminos_propios(actividad):
    resultado = es_aceptacion_terminos_valida(
        actividad,
        actividad,
        True
    )

    assert resultado is True


def test_tyc_04_rechaza_aceptacion_omitida():
    resultado = es_aceptacion_terminos_valida(
        "Tirolesa",
        "Tirolesa",
        None
    )

    assert resultado is False
