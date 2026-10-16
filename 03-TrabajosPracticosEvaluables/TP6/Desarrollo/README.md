
# EcoHarmony Park — TP 6 TDD

Proyecto de Ingeniería y Calidad de Software — UTN FRC.

Historia de usuario: Inscribirme a actividad.

## Tecnologías

- Python 3.12+
- pytest

## Configuración inicial

Desde la carpeta `Desarrollo`:

1. Crear el entorno virtual:

   python -m venv .venv

2. Instalar las dependencias:

   .\.venv\Scripts\python.exe -m pip install -e ".[dev]"

3. Ejecutar las pruebas:

   .\.venv\Scripts\python.exe -m pytest

## Metodología

El backend se desarrolla mediante ciclos RED–GREEN–REFACTOR.

Las pruebas se incorporan incrementalmente y se conserva
el historial de Git como evidencia de los ciclos TDD.
