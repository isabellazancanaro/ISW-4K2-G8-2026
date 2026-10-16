
from ecoharmony.terminos import es_aceptacion_terminos_valida


def test_tyc_01_aceptar_terminos_correctos_tirolesa():
    resultado = es_aceptacion_terminos_valida(
        "Tirolesa",
        "Tirolesa",
        True
    )

    assert resultado is True
