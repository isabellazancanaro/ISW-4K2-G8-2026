from dataclasses import dataclass, field
from datetime import datetime

from ecoharmony.inscripciones import Inscripcion
from ecoharmony.models.visitante import Visitante


@dataclass(frozen=True)
class ParticipanteConfirmado:
    visitante: Visitante
    codigo_qr: str


@dataclass(frozen=True)
class Correo:
    destinatario: str
    numero_orden: str
    actividad: str
    inicio: datetime
    participantes: tuple[ParticipanteConfirmado, ...]


@dataclass
class NotificadorSimulado:
    enviados: list[Correo] = field(default_factory=list)

    def enviar(self, correo: Correo) -> None:
        self.enviados.append(correo)


class ServicioConfirmaciones:
    def __init__(self, notificador: NotificadorSimulado) -> None:
        self._notificador = notificador
        self._ultimo_numero = 0

    def confirmar(self, inscripcion: Inscripcion, email_titular: str) -> None:
        self._ultimo_numero += 1
        numero_orden = f"ORD-{self._ultimo_numero:04d}"

        participantes = tuple(
            ParticipanteConfirmado(
                visitante=visitante,
                codigo_qr=(
                    f"{numero_orden}|{visitante.dni}|"
                    f"{inscripcion.actividad}|{inscripcion.inicio.isoformat()}"
                ),
            )
            for visitante in inscripcion.visitantes
        )

        self._notificador.enviar(
            Correo(
                destinatario=email_titular,
                numero_orden=numero_orden,
                actividad=inscripcion.actividad,
                inicio=inscripcion.inicio,
                participantes=participantes,
            )
        )