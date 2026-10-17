from dataclasses import dataclass, field

from ecoharmony.inscripciones import Inscripcion


@dataclass(frozen=True)
class Correo:
    destinatario: str


@dataclass
class NotificadorSimulado:
    enviados: list[Correo] = field(default_factory=list)

    def enviar(self, correo: Correo) -> None:
        self.enviados.append(correo)


class ServicioConfirmaciones:
    def __init__(self, notificador: NotificadorSimulado) -> None:
        self._notificador = notificador

    def confirmar(self, inscripcion: Inscripcion, email_titular: str) -> None:
        self._notificador.enviar(Correo(destinatario=email_titular))
        