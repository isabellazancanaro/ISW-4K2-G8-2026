from datetime import datetime

from ecoharmony.anticipacion import esta_en_ventana_de_reserva


def test_ant_01_reserva_exactamente_24_horas_antes_permitida():
    inicio = datetime.fromisoformat("2026-10-20T09:00:00-03:00")
    ahora = datetime.fromisoformat("2026-10-19T09:00:00-03:00")

    assert esta_en_ventana_de_reserva(inicio, ahora) is True


def test_ant_02_reserva_exactamente_15_minutos_antes_permitida():
    inicio = datetime.fromisoformat("2026-10-20T09:00:00-03:00")
    ahora = datetime.fromisoformat("2026-10-20T08:45:00-03:00")

    assert esta_en_ventana_de_reserva(inicio, ahora) is True
