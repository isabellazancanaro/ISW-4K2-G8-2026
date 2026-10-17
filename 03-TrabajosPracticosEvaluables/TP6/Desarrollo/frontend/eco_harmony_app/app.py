"""Adaptador HTTP del dominio EcoHarmony; estado local a cada aplicación."""

from base64 import b64encode
from datetime import date, datetime, timedelta, timezone
from threading import RLock

from flask import Flask, abort, jsonify, redirect, render_template, request, url_for

from ecoharmony.actividades import ACTIVIDADES, es_actividad_valida
from ecoharmony.confirmaciones import NotificadorSimulado, ServicioConfirmaciones
from ecoharmony.inscripciones import ServicioInscripciones
from ecoharmony.models.visitante import Visitante
from ecoharmony.talles import TALLES_VALIDOS

from .horarios import dias_inscribibles, horas_inscribibles

ZONA = timezone(timedelta(hours=-3))
TALLES = tuple(sorted(TALLES_VALIDOS, key=("XS", "S", "M", "L", "XL", "XXL").index))


def crear_app(config=None):
    app = Flask(__name__)
    app.config.from_mapping(RELOJ=lambda: datetime.now(ZONA))
    if config:
        app.config.update(config)

    notificador = NotificadorSimulado()
    servicio = ServicioInscripciones(ServicioConfirmaciones(notificador))
    confirmaciones = {}
    bloqueo = RLock()
    app.extensions["ecoharmony"] = {
        "servicio": servicio, "notificador": notificador,
        "confirmaciones": confirmaciones,
    }

    def ahora_actual():
        ahora = app.config["RELOJ"]()
        if ahora.tzinfo is None or ahora.utcoffset() is None:
            raise ValueError("El reloj de la aplicación debe incluir zona horaria")
        return ahora.astimezone(ZONA)

    def formulario(error=None, estado=200):
        actividades = [
            {
                "id": i, "nombre": actividad.nombre,
                "cupo": actividad.capacidad_maxima, "edad_minima": actividad.edad_minima,
                "requiere_vestimenta": int(actividad.requiere_talle),
                "terminos": f"Términos y condiciones de {actividad.nombre} (provisorio; pendiente de validación docente)",
            }
            for i, actividad in enumerate(ACTIVIDADES.values(), 1)
        ]
        return render_template(
            "inscripcion.html", actividades=actividades,
            dias=dias_inscribibles(ahora_actual()), talles=TALLES,
            error=error, valores=request.form.to_dict(flat=False),
        ), estado

    @app.get("/")
    def inicio():
        return render_template("inicio.html")

    @app.get("/inscripcion")
    def formulario_inscripcion():
        return formulario()

    @app.post("/inscripcion")
    def inscribir():
        form = request.form
        try:
            turno = datetime.fromisoformat(form.get("turno", ""))
            # El datetime-local del navegador no incluye offset: es hora del parque.
            if turno.tzinfo is None:
                turno = turno.replace(tzinfo=ZONA)
            turno = turno.astimezone(ZONA)
            cantidad = int(form.get("cantidad", ""))
            nombres = form.getlist("nombre")
            dnis = form.getlist("dni")
            edades = form.getlist("edad")
            talles = form.getlist("talle")
            if not (len(nombres) == len(dnis) == len(edades)):
                raise ValueError("Los datos de los participantes están incompletos")
            if talles and len(talles) != len(dnis):
                raise ValueError("Faltan talles de participantes")
            visitantes = [
                Visitante(nombre, dni, int(edad), (talles[i] or None) if talles else None)
                for i, (nombre, dni, edad) in enumerate(zip(nombres, dnis, edades))
            ]
            email = form.get("email", "").strip()
            # Comprobación de entrada del titular; el dominio no valida este campo.
            if (len(email.split("@")) != 2 or not all(email.split("@"))
                    or any(c.isspace() for c in email)):
                raise ValueError("Email del titular inválido")
        except (ValueError, OverflowError):
            return formulario(
                "Revisá el turno, la cantidad, las edades, los datos de cada participante y el email del titular.",
                400,
            )

        # Serializa acceso al estado en este proceso; no proporciona persistencia.
        with bloqueo:
            try:
                resultado = servicio.inscribir(
                    actividad=form.get("actividad", ""), inicio=turno,
                    ahora=ahora_actual(), cantidad=cantidad, visitantes=visitantes,
                    actividad_terminos=form.get("actividad", ""),
                    acepto_terminos=form.get("terminos") == "1", email_titular=email,
                )
            except Exception:
                app.logger.exception("Falló la confirmación de la inscripción")
                return formulario(
                    "No se pudo emitir la confirmación. La reserva no quedó registrada; intentá nuevamente.",
                    503,
                )
            if resultado is None:
                return formulario(
                    "No se pudo confirmar la inscripción. Revisá los datos, los términos, el turno, los cupos y posibles superposiciones.",
                    422,
                )
            inscripcion_id = len(confirmaciones) + 1
            confirmaciones[inscripcion_id] = notificador.enviados[-1]
        return redirect(url_for("confirmacion", inscripcion_id=inscripcion_id))

    @app.get("/inscripcion/<int:inscripcion_id>")
    def confirmacion(inscripcion_id):
        with bloqueo:
            correo = confirmaciones.get(inscripcion_id)
        if correo is None:
            abort(404)
        inscripcion = {
            "id": inscripcion_id, "numero_orden": correo.numero_orden,
            "actividad": correo.actividad, "turno": correo.inicio.isoformat(timespec="minutes"),
            "email": correo.destinatario,
        }
        visitantes = [
            {
                "id": i, "nombre": p.visitante.nombre, "dni": p.visitante.dni,
                "edad": p.visitante.edad, "talle": p.visitante.talle,
                "codigo_qr": p.codigo_qr,
                "qr_data_uri": "data:image/png;base64," + b64encode(p.imagen_qr).decode("ascii"),
            }
            for i, p in enumerate(correo.participantes, 1)
        ]
        return render_template(
            "confirmacion.html", inscripcion=inscripcion, visitantes=visitantes, correo=correo,
        )

    @app.get("/api/horarios")
    def api_horarios():
        try:
            dia = date.fromisoformat(request.args.get("fecha", ""))
        except ValueError:
            return jsonify(error="Fecha inválida"), 400
        actividad = request.args.get("actividad", "")
        if not es_actividad_valida(actividad):
            return jsonify(error="La actividad seleccionada no existe"), 404
        with bloqueo:
            horarios = [
                {
                    # Conserva el formato datetime-local que consume el formulario.
                    "valor": turno.replace(tzinfo=None).isoformat(timespec="minutes"),
                    "texto": f"{turno:%H:%M}",
                    "disponibles": servicio.consultar_cupos(actividad, turno),
                }
                for turno in horas_inscribibles(dia, ahora_actual())
            ]
        return jsonify(horarios)

    return app


app = crear_app()
