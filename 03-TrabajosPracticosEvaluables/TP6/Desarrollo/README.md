
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


## Subgrupo 3 — Inscripción a actividades

### Funcionalidades

El backend permite:

- Registrar inscripciones individuales y grupales.
- Validar actividades, fechas, horarios y anticipación.
- Validar cantidad, datos personales, edades y talles.
- Verificar aceptación de términos y condiciones.
- Consultar y actualizar los cupos por actividad y turno.
- Rechazar inscripciones con horarios superpuestos.
- Rechazar solicitudes grupales completas si algún integrante no cumple los requisitos.
- Conservar inscripciones confirmadas en memoria.
- Generar confirmaciones con un código QR por participante.
- Simular el envío de un único correo al titular.

### Estructura principal

- `inscripciones.py`: servicio central y registro de inscripciones.
- `superposiciones.py`: detección de conflictos horarios.
- `confirmaciones.py`: generación de confirmaciones y notificador simulado.
- `codigos_qr.py`: generación de imágenes QR en formato PNG.

### Instalación

Se requiere Python 3.12 o superior.

Desde la carpeta `Desarrollo`:

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -e ".\backend[dev]"
```

### Ejecución de pruebas

```powershell
.\.venv\Scripts\python.exe -m pytest -v .\backend\tests
```

### Uso del servicio de inscripciones

```python
from datetime import datetime, timedelta, timezone

from ecoharmony.inscripciones import ServicioInscripciones
from ecoharmony.models.visitante import Visitante
from ecoharmony.confirmaciones import (
    ServicioConfirmaciones,
    NotificadorSimulado,
)

zona = timezone(timedelta(hours=-3))

inicio = datetime(2026, 10, 20, 10, 0, tzinfo=zona)
ahora = datetime(2026, 10, 19, 12, 0, tzinfo=zona)

notificador = NotificadorSimulado()
confirmaciones = ServicioConfirmaciones(notificador)

servicio = ServicioInscripciones(
    servicio_confirmaciones=confirmaciones
)

visitante = Visitante(
    nombre="Ana García",
    dni="12345678",
    edad=20,
    talle="M",
)

resultado = servicio.inscribir(
    actividad="Tirolesa",
    inicio=inicio,
    ahora=ahora,
    cantidad=1,
    visitantes=[visitante],
    actividad_terminos="Tirolesa",
    acepto_terminos=True,
    email_titular="titular@example.com",
)

if resultado is not None:
    print("Inscripción confirmada")
    print("Cupos restantes:", servicio.consultar_cupos("Tirolesa", inicio))
    print("Correos simulados:", len(notificador.enviados))
else:
    print("Inscripción rechazada")
```

### Contrato para el frontend

`ServicioInscripciones.inscribir()` devuelve:

- Una instancia de `Inscripcion` cuando se confirma correctamente.
- `None` cuando alguna validación de negocio falla.

`ServicioInscripciones.consultar_cupos(actividad, inicio)` devuelve la cantidad de lugares disponibles.

`ServicioInscripciones.inscripciones` permite consultar las inscripciones registradas.

El correo se envía al titular indicado mediante `email_titular`, utilizando el servicio de confirmaciones configurado.

### Limitaciones

- El almacenamiento es en memoria: los datos no sobreviven al reinicio del proceso.
- No se utiliza una base de datos real.
- Los correos se simulan y no se envían a direcciones reales.
- El frontend debe proporcionar un email del titular.
- Los términos y condiciones definitivos están pendientes de validación docente.
- El control de ocupación en memoria no implementa protección frente a inscripciones concurrentes.
- La gestión de fallos de confirmación revierte el estado local, pero no garantiza una transacción distribuida con un proveedor de correo externo.
```
