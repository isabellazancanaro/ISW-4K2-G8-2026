from datetime import datetime, timedelta

from db import conectar

manana = datetime.now().date() + timedelta(days=1)


def turno(hora):
    return datetime(manana.year, manana.month, manana.day, hora).isoformat(timespec="minutes")


def inscribir(conexion, actividad, hora, cantidad, dni_inicial):
    actividad_id = conexion.execute(
        "SELECT id FROM actividades WHERE nombre = ?", (actividad,)
    ).fetchone()["id"]
    cursor = conexion.execute(
        """INSERT INTO inscripciones (actividad_id, turno, email)
           VALUES (?, ?, 'prueba@mail.com')""",
        (actividad_id, turno(hora)),
    )
    for i in range(cantidad):
        conexion.execute(
            "INSERT INTO visitantes (inscripcion_id, dni, edad) VALUES (?, ?, 30)",
            (cursor.lastrowid, str(dni_inicial + i)),
        )


conexion = conectar()
conexion.execute("DELETE FROM inscripciones WHERE email = 'prueba@mail.com'")  # borra visitantes en cascada

inscribir(conexion, "Tirolesa", 10, 10, 20000000)  # 10/10 -> completo
inscribir(conexion, "Tirolesa", 11, 7, 21000000)   # 7/10 -> quedan 3
inscribir(conexion, "Safari", 10, 2, 22000000)     # 2/8 -> quedan 6

conexion.commit()
conexion.close()
print(f"Datos de prueba cargados para {manana}")