def ocupados_por_turno(conexion, actividad_id, dia):
    """{'2026-10-16T10:00': 7, ...}: visitantes con inscripción activa, por turno de ese día."""
    filas = conexion.execute(
        """SELECT i.turno, COUNT(v.id) AS ocupados
           FROM inscripciones i
           JOIN visitantes v ON v.inscripcion_id = i.id
           WHERE i.actividad_id = ?
             AND i.estado = 'activa'
             AND substr(i.turno, 1, 10) = ?
           GROUP BY i.turno""",
        (actividad_id, dia.isoformat()),
    ).fetchall()
    return {fila["turno"]: fila["ocupados"] for fila in filas}