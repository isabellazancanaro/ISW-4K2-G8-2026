from datetime import datetime, timedelta, timezone

from ecoharmony.confirmaciones import NotificadorSimulado, ServicioConfirmaciones
from ecoharmony.inscripciones import Inscripcion
from ecoharmony.models.visitante import Visitante

ZONA_ARGENTINA = timezone(timedelta(hours=-3))
MARTES_10 = datetime(2026, 10, 20, 10, 0, tzinfo=ZONA_ARGENTINA)
EMAIL_TITULAR = "titular@ecoharmony.test"


def test_mail_01_confirmacion_exitosa_solicita_un_correo():
    """MAIL-01: confirmar una inscripción válida solicita el envío del correo."""
    inscripcion = Inscripcion(
        actividad="Tirolesa",
        inicio=MARTES_10,
        visitantes=[Visitante(nombre="Ana García", dni="12345678", edad=20, talle="M")],
    )
    notificador = NotificadorSimulado()
    servicio = ServicioConfirmaciones(notificador)

    servicio.confirmar(inscripcion, EMAIL_TITULAR)

    assert len(notificador.enviados) == 1