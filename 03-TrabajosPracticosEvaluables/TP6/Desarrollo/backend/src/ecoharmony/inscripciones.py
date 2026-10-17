
from dataclasses import dataclass
from datetime import datetime

from ecoharmony.actividades import es_actividad_valida
from ecoharmony.anticipacion import esta_en_ventana_de_reserva
from ecoharmony.calendario import es_fecha_habilitada
from ecoharmony.cantidad_participantes import cantidad_coincide_con_visitantes
from ecoharmony.datos_visitante import identificaciones_grupo_validas
from ecoharmony.disponibilidad import consultar_disponibilidad
from ecoharmony.edades import es_edad_valida_para_actividad
from ecoharmony.horarios import es_horario_valido
from ecoharmony.models.visitante import Visitante
from ecoharmony.talles import es_talle_valido_para_actividad
from ecoharmony.terminos import es_aceptacion_terminos_valida
from ecoharmony.superposiciones import tiene_superposicion_grupo

@dataclass(frozen=True)
class Inscripcion:
    actividad: str
    inicio: datetime
    visitantes: list[Visitante]


class ServicioInscripciones:

    def __init__(self, servicio_confirmaciones=None):
        self._inscripciones: list[Inscripcion] = []
        self.ocupacion: dict[tuple[str, datetime], int] = {}
        self._servicio_confirmaciones = servicio_confirmaciones

    @property
    def inscripciones(self) -> tuple[Inscripcion, ...]:
        return tuple(self._inscripciones)

    def consultar_cupos(
        self,
        actividad: str,
        inicio: datetime,
    ) -> int:
        return consultar_disponibilidad(
            actividad,
            inicio,
            self.ocupacion,
        )

    
    def _solicitud_valida(
        self,
        actividad: str,
        inicio: datetime,
        ahora: datetime,
        cantidad: int,
        visitantes: list[Visitante],
        actividad_terminos: str,
        acepto_terminos: bool,
    ) -> bool:

        if not es_actividad_valida(actividad):
            return False

        if not es_fecha_habilitada(inicio.date()):
            return False

        if not es_horario_valido(inicio.time()):
            return False

        if not esta_en_ventana_de_reserva(inicio, ahora):
            return False

        if not cantidad_coincide_con_visitantes(
            cantidad, visitantes
        ):
            return False

        if not identificaciones_grupo_validas(visitantes):
            return False

        for visitante in visitantes:
            if not es_edad_valida_para_actividad(
                actividad, visitante.edad
            ):
                return False

            if not es_talle_valido_para_actividad(
                actividad, visitante.talle
            ):
                return False

        if not es_aceptacion_terminos_valida(
            actividad,
            actividad_terminos,
            acepto_terminos,
        ):
            return False

        return True

    def inscribir(
        self,
        actividad: str,
        inicio: datetime,
        ahora: datetime,
        cantidad: int,
        visitantes: list[Visitante],
        actividad_terminos: str,
        acepto_terminos: bool,
        email_titular: str | None = None,
    ) -> Inscripcion | None:
        
        if not self._solicitud_valida(
            actividad,
            inicio,
            ahora,
            cantidad,
            visitantes,
            actividad_terminos,
            acepto_terminos,
        ):
            return None

        if self.consultar_cupos(actividad, inicio) < cantidad:
            return None

        if tiene_superposicion_grupo(
            visitantes,
            inicio,
            self._inscripciones,
        ):
            return None
        
        inscripcion = Inscripcion(
            actividad=actividad,
            inicio=inicio,
            visitantes=list(visitantes),
        )

        
        clave = (actividad, inicio)

        # Registrar la inscripción y actualizar la ocupación.
        self._inscripciones.append(inscripcion)
        self.ocupacion[clave] = (
            self.ocupacion.get(clave, 0) + cantidad
        )

        try:
            if (
                self._servicio_confirmaciones is not None
                and email_titular is not None
            ):
                self._servicio_confirmaciones.confirmar(
                    inscripcion,
                    email_titular,
                )

        except Exception:
            # Revertir el registro si falla la confirmación.
            self._inscripciones.remove(inscripcion)
            self.ocupacion[clave] -= cantidad

            if self.ocupacion[clave] == 0:
                del self.ocupacion[clave]

            raise

        return inscripcion
