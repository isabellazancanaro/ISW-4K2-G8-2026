from datetime import time

from ecoharmony.horarios import es_horario_valido


def test_hor_01_primer_turno_permitido():
    hora = time(9, 0)

    resultado = es_horario_valido(hora)

    assert resultado is True