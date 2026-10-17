import sqlite3
from pathlib import Path

RUTA_DB = Path(__file__).parent / "eco_harmony.db"


def conectar():
    conexion = sqlite3.connect(RUTA_DB)
    conexion.row_factory = sqlite3.Row  # permite leer cada columna por nombre
    conexion.execute("PRAGMA foreign_keys = ON")  # sin esto SQLite no respeta las FK
    return conexion