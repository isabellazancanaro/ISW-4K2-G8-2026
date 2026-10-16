
# EcoHarmony Park — TP 6 TDD

Proyecto de Ingeniería y Calidad de Software — UTN FRC.

**Historia de usuario:** Inscribirme a actividad.

## Tecnologías

- Python 3.12+
- pytest
- Interfaz web responsive (pendiente de implementación)

## Estructura del proyecto

- `backend/`: lógica de negocio y pruebas automatizadas.
  - `src/ecoharmony/`: módulos del sistema.
  - `tests/`: pruebas automatizadas.
  - `pyproject.toml`: configuración del proyecto Python.
- `frontend/`: interfaz web responsive (pendiente de desarrollo).

## Configuración inicial

Desde la carpeta `Desarrollo`:

1. Crear el entorno virtual:

   ```powershell
   python -m venv .venv
   ```

2. Instalar las dependencias:

   ```powershell
   .\.venv\Scripts\python.exe -m pip install -e ".\backend[dev]"
   ```

3. Ejecutar las pruebas:

   ```powershell
   .\.venv\Scripts\python.exe -m pytest -v .\backend\tests
   ```

## Metodología

El backend se desarrolla mediante ciclos RED–GREEN–REFACTOR.

Las pruebas se incorporan incrementalmente y se conserva el historial de Git como evidencia de los ciclos TDD.

El diseño seguirá un enfoque principalmente orientado a objetos, incorporando modelos y responsabilidades progresivamente, sin crear clases innecesarias.
