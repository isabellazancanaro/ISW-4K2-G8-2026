from datetime import time

from ecoharmony.horarios import es_horario_valido


def test_hor_01_primer_turno_permitido():
    hora = time(9, 0)

    resultado = es_horario_valido(hora)

    assert resultado is True


def test_hor_02_ultimo_turno_permitido():
    hora = time(17, 0)

    resultado = es_horario_valido(hora)

    assert resultado is True


def test_hor_03_antes_primer_turno():
    hora = time(8, 0)

    resultado = es_horario_valido(hora)

    assert resultado is False


def test_hor_04_despues_ultimo_turno():
    hora = time(18, 0)

    resultado = es_horario_valido(hora)

    assert resultado is False


def test_hor_05_horario_no_alineado():
    hora = time(9, 30)

    resultado = es_horario_valido(hora)

    assert resultado is False


def test_hor_06_horario_omitido():
    hora = None

    resultado = es_horario_valido(hora)

    assert resultado is False