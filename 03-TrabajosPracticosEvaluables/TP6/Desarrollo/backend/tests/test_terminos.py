
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
