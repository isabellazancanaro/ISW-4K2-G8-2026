from db import conectar

conexion = conectar()

conexion.execute("""
    CREATE TABLE IF NOT EXISTS actividades (
        id                  INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre              TEXT    NOT NULL UNIQUE,
        cupo                INTEGER NOT NULL,
        edad_minima         INTEGER NOT NULL DEFAULT 0,
        requiere_vestimenta INTEGER NOT NULL DEFAULT 0
                            CHECK (requiere_vestimenta IN (0, 1)),
        terminos            TEXT    NOT NULL
    )
""")

conexion.execute("""
    CREATE TABLE IF NOT EXISTS inscripciones (
        id                 INTEGER PRIMARY KEY AUTOINCREMENT,
        actividad_id       INTEGER NOT NULL REFERENCES actividades(id),
        turno              TEXT    NOT NULL,
        email              TEXT    NOT NULL,
        terminos_aceptados INTEGER NOT NULL CHECK (terminos_aceptados IN (0, 1)),
        estado             TEXT    NOT NULL DEFAULT 'activa'
                           CHECK (estado IN ('activa', 'cancelada')),
        creada_en          TEXT    NOT NULL DEFAULT CURRENT_TIMESTAMP
    )
""")

conexion.execute("""
    CREATE TABLE IF NOT EXISTS visitantes (
        id             INTEGER PRIMARY KEY AUTOINCREMENT,
        inscripcion_id INTEGER NOT NULL
                       REFERENCES inscripciones(id) ON DELETE CASCADE,
        dni            TEXT    NOT NULL,
        edad           INTEGER NOT NULL,
        nombre         TEXT,
        talle          TEXT
    )
""")

conexion.executemany(
    """INSERT OR IGNORE INTO actividades
       (nombre, cupo, edad_minima, requiere_vestimenta, terminos)
       VALUES (?, ?, ?, ?, ?)""",
    [
        ("Tirolesa",   10, 8,  1, "Términos y condiciones de Tirolesa (provisorio)"),
        ("Safari",      8, 0,  0, "Términos y condiciones de Safari (provisorio)"),
        ("Palestra",   12, 12, 1, "Términos y condiciones de Palestra (provisorio)"),
        ("Jardinería", 12, 0,  0, "Términos y condiciones de Jardinería (provisorio)"),
    ],
)

conexion.commit()
conexion.close()
print("Base creada")