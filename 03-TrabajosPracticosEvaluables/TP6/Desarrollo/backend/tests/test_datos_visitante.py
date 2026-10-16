from ecoharmony.datos_visitante import identificacion_visitante_valida
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