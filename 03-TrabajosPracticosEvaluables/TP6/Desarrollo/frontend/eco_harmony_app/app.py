from datetime import date, datetime

from flask import (Flask, abort, jsonify, redirect, render_template, request,
                   url_for)

from cupos import ocupados_por_turno
from db import conectar
from horarios import dias_inscribibles, horas_inscribibles

app = Flask(__name__)

TALLES = ("XS", "S", "M", "L", "XL", "XXL")


def ahora_actual():
    # SOLO PARA PROBAR: ?ahora=2026-10-16T09:30 simula otra hora. Se borra al terminar.
    try:
        return datetime.fromisoformat(request.args["ahora"])
    except (KeyError, ValueError):
        return datetime.now()


@app.get("/")
def inicio():
    return render_template("inicio.html")


@app.get("/inscripcion")
def formulario_inscripcion():
    conexion = conectar()
    actividades = conexion.execute(
        """SELECT id, nombre, cupo, requiere_vestimenta, terminos
           FROM actividades ORDER BY id"""
    ).fetchall()
    conexion.close()

    return render_template(
        "inscripcion.html",
        actividades=actividades,
        dias=dias_inscribibles(ahora_actual()),
        talles=TALLES,
    )


@app.post("/inscripcion")
def inscribir():
    # SIN VALIDAR NADA (a propósito): guarda lo que llegue.
    form = request.form
    conexion = conectar()

    actividad = conexion.execute(
        "SELECT id FROM actividades WHERE nombre = ?",
        (form.get("actividad", ""),),
    ).fetchone()

    cursor = conexion.execute(
        """INSERT INTO inscripciones (actividad_id, turno, email)
           VALUES (?, ?, ?)""",
        (
            actividad["id"],
            form.get("turno", ""),
            form.get("email", ""),
        ),
    )
    inscripcion_id = cursor.lastrowid

    # Cada persona manda un valor por campo, siempre en el mismo orden.
    nombres = form.getlist("nombre")
    dnis = form.getlist("dni")
    edades = form.getlist("edad")
    talles = form.getlist("talle")  # vacía si la actividad no usa talle

    for i, dni in enumerate(dnis):
        conexion.execute(
            """INSERT INTO visitantes (inscripcion_id, dni, edad, nombre, talle)
               VALUES (?, ?, ?, ?, ?)""",
            (
                inscripcion_id,
                dni,
                edades[i],
                nombres[i] or None,
                (talles[i] if talles else None) or None,
            ),
        )

    conexion.commit()  # todo o nada: si algo falla antes, no se guarda nada
    conexion.close()
    return redirect(url_for("confirmacion", inscripcion_id=inscripcion_id))


@app.get("/inscripcion/<int:inscripcion_id>")
def confirmacion(inscripcion_id):
    conexion = conectar()
    inscripcion = conexion.execute(
        """SELECT i.id, i.turno, i.email, a.nombre AS actividad
           FROM inscripciones i
           JOIN actividades a ON a.id = i.actividad_id
           WHERE i.id = ?""",
        (inscripcion_id,),
    ).fetchone()
    visitantes = conexion.execute(
        """SELECT id, nombre, dni, edad, talle
           FROM visitantes WHERE inscripcion_id = ? ORDER BY id""",
        (inscripcion_id,),
    ).fetchall()
    conexion.close()

    if inscripcion is None:
        abort(404)
    return render_template(
        "confirmacion.html", inscripcion=inscripcion, visitantes=visitantes
    )


@app.get("/api/horarios")
def api_horarios():
    try:
        dia = date.fromisoformat(request.args.get("fecha", ""))
    except ValueError:
        return jsonify(error="Fecha inválida"), 400

    conexion = conectar()
    actividad = conexion.execute(
        "SELECT id, cupo FROM actividades WHERE nombre = ?",
        (request.args.get("actividad", ""),),
    ).fetchone()
    if actividad is None:
        conexion.close()
        return jsonify(error="La actividad seleccionada no existe"), 404

    ocupados = ocupados_por_turno(conexion, actividad["id"], dia)
    conexion.close()

    horarios = []
    for turno in horas_inscribibles(dia, ahora_actual()):
        valor = turno.isoformat(timespec="minutes")  # '2026-10-16T10:00'
        horarios.append({
            "valor": valor,
            "texto": f"{turno:%H:%M}",
            "disponibles": actividad["cupo"] - ocupados.get(valor, 0),
        })
    return jsonify(horarios)