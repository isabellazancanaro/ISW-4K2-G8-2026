
# EcoHarmony Park — TP 6 TDD

Proyecto de Ingeniería y Calidad de Software — UTN FRC.

**Historia de usuario:** Inscribirme a actividad.

## Tecnologías

- Python 3.12+
- pytest
- Flask + Jinja2 para la interfaz web responsive (integración SG4)

## Estructura del proyecto

- `backend/`: lógica de negocio y pruebas automatizadas.
  - `src/ecoharmony/`: módulos del sistema.
  - `tests/`: pruebas automatizadas.
  - `pyproject.toml`: configuración del proyecto Python.
- `frontend/eco_harmony_app/`: rutas Flask, plantillas y recursos visuales.
- `frontend/tests/`: pruebas de integración HTTP y confirmaciones.

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


## Subgrupo 4 — Integración web local

La aplicación importa el paquete instalado `ecoharmony`. Las rutas Flask no
registran datos en SQLite: utilizan un `ServicioInscripciones` y un
`NotificadorSimulado` compartidos entre peticiones de la misma aplicación.
Los scripts SQLite de la primera maqueta fueron retirados. Si existe un
`eco_harmony.db` local de esa maqueta, no se consulta ni se migra.

### Instalación y arranque

Ejecutar todos los comandos desde `03-TrabajosPracticosEvaluables/TP6/Desarrollo`.
En macOS/Linux, con Python 3.12 o superior:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -e './backend[dev,web]'
.venv/bin/python -m flask --app frontend.eco_harmony_app.app run --host 127.0.0.1 --port 5000
```

En Windows PowerShell:

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -e ".\backend[dev,web]"
.\.venv\Scripts\python.exe -m flask --app frontend.eco_harmony_app.app run --host 127.0.0.1 --port 5000
```

Abrir http://127.0.0.1:5000. No se necesita crear ni cargar una base de datos.
Detener el servidor con Ctrl+C. El extra `web` declara Flask; `dev` declara
pytest y el lector de QR usado por las pruebas.

### Pruebas

```bash
.venv/bin/python -m pytest -q backend/tests frontend/tests
```

En PowerShell usar `.\.venv\Scripts\python.exe` en lugar de `.venv/bin/python`.
Las pruebas web usan `crear_app({"TESTING": True, "RELOJ": lambda: ahora})`, con
un datetime consciente de zona horaria. Cada aplicación tiene estado propio.
Comprueban reservas individuales/grupales, lectura de PNG QR, rechazos sin
efectos, superposiciones, cupos, peticiones consecutivas y fallos de confirmación.
No modifican las pruebas heredadas del dominio.

### Contrato de rutas y formularios para las pantallas

Se conservan `/`, GET y POST `/inscripcion`, GET `/api/horarios` y
GET `/inscripcion/<int:inscripcion_id>`. El identificador de URL es un entero
local; el número de orden de negocio es `ORD-0001`, etc.

POST `/inscripcion` recibe:

| Campo | Formato |
| --- | --- |
| `actividad` | Nombre exacto del catálogo, con tildes |
| `turno` | ISO datetime; si no tiene offset se interpreta como UTC−03:00 |
| `cantidad` | Entero positivo declarado, que el dominio compara con los visitantes |
| `email` | Email del titular; obligatorio para solicitar el correo simulado |
| `terminos` | `"1"` al aceptar; ausente o distinto implica no aceptación |
| `nombre`, `dni`, `edad` | Campos repetidos, con igual longitud y orden |
| `talle` | Campo repetido para Tirolesa/Palestra; ausente para Safari/Jardinería |

El adaptador convierte edades y cantidad a enteros, pero conserva DNI como
texto. Las reglas de identificación, edad, vestimenta, fechas, términos,
capacidad y superposición siguen siendo autoridad del backend.
El email recibe una comprobación básica de estructura, sin verificar su existencia.

GET `/api/horarios?actividad=Safari&fecha=2026-10-20` devuelve una lista:

```json
[{"valor": "2026-10-20T10:00", "texto": "10:00", "disponibles": 8}]
```

Un día cerrado o fuera de ventana devuelve `[]`; una fecha mal formada devuelve
400 y una actividad inexistente 404, con JSON `{"error": "mensaje"}`.
La generación de opciones reutiliza calendario, horarios y anticipación del
backend. El parámetro de URL `ahora` de la maqueta ya no modifica el reloj.

### Contrato exacto de contexto Jinja para Juan Cruz

`inscripcion.html` conserva `actividades`, `dias` y `talles`.
Cada actividad es un diccionario con `id`, `nombre`, `cupo`,
`requiere_vestimenta` (0/1), `edad_minima` y `terminos` provisional.
`dias` sigue siendo una lista de pares `(valor ISO, etiqueta)`.
Se añaden:

- `error`: texto o `None`. Mostrarlo como aviso accesible, sin usar `safe`.
- `valores`: diccionario de listas de strings, por ejemplo
  `{"actividad": ["Safari"], "nombre": ["Ana", "Luis"], "terminos": ["1"]}`.
  En GET es `{}`. Usarlo para reconstruir campos y visitantes al rechazar.
  Nunca insertar estos datos con `innerHTML`; usar escape Jinja, `tojson`
  y propiedades DOM como `value` o `textContent`.

Errores de entrada HTTP devuelven el formulario con 400; rechazos del dominio,
con 422 y un mensaje general, porque `inscribir()` devuelve `None` sin causa.
Si falla la confirmación, devuelve 503; el servicio de dominio revierte el
registro y los cupos. El adaptador no presenta un rechazo como éxito.
En éxito redirige a la ruta de confirmación.

`confirmacion.html` recibe:

- `inscripcion`: diccionario con `id` (entero de URL), `numero_orden` (string),
  `actividad`, `turno` (ISO con offset) y `email`.
- `visitantes`: lista de diccionarios con `id` (posición desde 1), `nombre`,
  `dni`, `edad`, `talle`, `codigo_qr` (contenido codificado) y `qr_data_uri`
  (`data:image/png;base64,...`, imagen genuina generada por el backend).
- `correo`: objeto `Correo` del backend, con `destinatario`, `numero_orden`,
  `actividad`, `inicio` (datetime) y `participantes` (tupla de confirmados).
  Es evidencia de envío **simulado**, no de entrega de un email real.

La plantilla puede mostrar cada imagen con:

```html
<img src="{{ v['qr_data_uri'] }}" alt="QR de {{ v['nombre'] }}">
```

Una confirmación inexistente devuelve 404.

### Formulario y confirmación integrados

El formulario envía `cantidad` y aplica el máximo de cupos del turno consultado.
Si la cantidad es fraccionaria, menor a uno o superior a la disponibilidad,
no permite generar visitantes ni confirmar. El backend vuelve a validar los
cupos al registrar, por si la disponibilidad cambió desde la consulta.

Nombre, DNI, edad y el talle pertinente son obligatorios. DNI conserva ceros
iniciales y exige 7 u 8 dígitos; edad admite años enteros y respeta el mínimo
del catálogo. El nombre no puede estar vacío ni contener solamente espacios.
El email y la aceptación de términos son obligatorios. Los campos de confirmación
se habilitan después de generar una cantidad válida de visitantes.

Un rechazo muestra un aviso accesible y reconstruye los datos ingresados
cuando el turno sigue disponible. La confirmación muestra orden, participantes,
QR PNG descargables y el contenido del único correo simulado. No se envían
emails a una bandeja real.

Verificación manual en navegador local: cantidad 11 frente a 10 cupos bloqueada;
reserva correcta con QR y orden; nueva consulta con 9 cupos y cantidad 10
bloqueada; nombre vacío impide enviar; intento con DNI ya reservado en el mismo
turno rechazado con datos conservados. Las pruebas HTTP comprueban también el
HTML de confirmación y los errores visibles. Queda por ampliar la revisión
visual en distintos tamaños de pantalla para la entrega final.

### Estado, reloj y límites

- Reservas, cupos, números de orden y correos simulados desaparecen al reiniciar.
- El reloj real se suministra desde Flask en UTC−03:00; no se cambia el dominio.
- Un bloqueo local serializa consultas y registros del adaptador en un proceso.
  No usar varios procesos/workers esperando compartir este estado en memoria.
- No se envían correos reales ni hay pagos o importes.
- Los términos siguen siendo provisionales, pendientes de validación docente.
