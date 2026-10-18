# EcoHarmony Park — TP 6 TDD

Proyecto de Ingeniería y Calidad de Software — UTN FRC.

**Historia de usuario:** Inscribirme a actividad.

## Tecnologías y requisitos

- Python 3.12 o superior, con `pip` y soporte para entornos virtuales.
- Backend: paquete Python `ecoharmony`, con estado en memoria.
- Frontend: Flask + Jinja2, HTML, CSS responsive y JavaScript.
- QR: `qrcode[pil]`; pruebas del backend: pytest y `zxing-cpp`.
- Navegador actualizado. No se necesita Node.js, npm ni compilar el frontend.
- Internet durante la instalación de dependencias. La tipografía Lato se carga
  desde Google Fonts; si no hay conexión, se utiliza la fuente alternativa del CSS.

## Estructura del proyecto

```text
Desarrollo/
├── README.md
├── instrucciones.md
├── .gitignore
├── backend/
│   ├── pyproject.toml
│   ├── src/ecoharmony/
│   │   ├── models/                 # Entidades Actividad y Visitante
│   │   ├── inscripciones.py        # Registro y validación integral
│   │   ├── confirmaciones.py       # Confirmaciones y correo simulado
│   │   ├── codigos_qr.py           # Generación de QR PNG
│   │   └── ...                     # Catálogo y validadores de negocio
│   └── tests/                      # Pruebas de los subgrupos de backend
└── frontend/
    └── eco_harmony_app/
        ├── __init__.py
        ├── app.py                  # Aplicación Flask y rutas HTTP
        ├── horarios.py             # Opciones de turnos usando el dominio
        ├── terminos.json           # Textos por actividad de la propuesta del equipo
        ├── requirements.txt        # Dependencia Flask
        ├── templates/
        │   ├── inicio.html         # Pantalla de inicio
        │   ├── inscripcion.html    # Formulario de inscripción
        │   └── confirmacion.html   # Confirmación, QR y acceso al correo
        └── static/
            ├── styles.css          # Estilos y adaptación a celular
            ├── inscripcion.js      # Formulario dinámico y avisos de validación
            ├── confirmacion.js     # Ventana de correo y descarga de tarjetas QR
            └── logo.png
```

`.venv/` se crea localmente y no se entrega en Git. El frontend importa el
backend instalado; ambos funcionan dentro de una misma aplicación Flask.
No hay que iniciar un servidor de backend separado.

## Configuración inicial: backend y frontend

Todos los comandos se ejecutan desde esta carpeta, `Desarrollo/`.
Desde la raíz del repositorio, entrar primero con:

```bash
cd 03-TrabajosPracticosEvaluables/TP6/Desarrollo
```

### Windows — PowerShell

Crear el entorno virtual una sola vez:

```powershell
py -3 -m venv .venv
```

El Python seleccionado debe ser 3.12 o superior. Instalar backend, herramientas
de pruebas y dependencias de la web:

```powershell
.\.venv\Scripts\python.exe -m pip install -e ".\backend[dev,web]"
```

Levantar la web:

```powershell
.\.venv\Scripts\python.exe -m flask --app frontend.eco_harmony_app.app run --host 127.0.0.1 --port 5001
```

### macOS / Linux

Crear el entorno virtual una sola vez:

```bash
python3 -m venv .venv
```

Instalar backend, herramientas de pruebas y dependencias de la web:

```bash
.venv/bin/python -m pip install -e './backend[dev,web]'
```

Levantar la web:

```bash
.venv/bin/python -m flask --app frontend.eco_harmony_app.app run --host 127.0.0.1 --port 5001
```

### Abrir, detener y volver a ejecutar

Abrir **http://127.0.0.1:5001** en el navegador. El formulario está en
http://127.0.0.1:5001/inscripcion. Se usa 5001 para evitar el puerto 5000,
que puede estar ocupado por servicios de macOS.

Mantener la terminal abierta mientras se prueba la web. Para detenerla,
presionar **Ctrl+C**. Para volver a iniciarla, repetir solo el comando Flask
correspondiente al sistema operativo; no recrear el entorno virtual.
Los comandos usan directamente el Python del entorno, sin necesidad de activarlo.

El extra `[web]` instala Flask; `[dev]` instala las dependencias de pruebas.
`qrcode[pil]` se instala como dependencia del backend. El archivo
`frontend/eco_harmony_app/requirements.txt` también declara Flask, pero no hace
falta instalarlo aparte si ya se usó `[dev,web]`.

Para desarrollar con recarga automática, agregar `--debug` al comando Flask.
Sin esa opción, detener y volver a iniciar Flask después de cambiar Python o
plantillas: una recarga del navegador puede seguir mostrando una plantilla
que el servidor conserva en memoria. Los reinicios borran las reservas de prueba.
Si un JavaScript o CSS sigue apareciendo desactualizado, hacer una recarga
forzada del navegador (Ctrl+Shift+R o Cmd+Shift+R).

### Ejecutar las pruebas del backend

Windows:

```powershell
.\.venv\Scripts\python.exe -m pytest -q backend/tests
```

macOS / Linux:

```bash
.venv/bin/python -m pytest -q backend/tests
```

La suite heredada contiene **98 ejecuciones**. El frontend se verifica
manualmente desde el navegador; no se incluyen pruebas automatizadas de frontend.

## Uso del frontend

1. En el inicio, elegir **Inscribirme a actividad**.
2. Seleccionar actividad, día y turno. Cada turno muestra sus cupos disponibles.
3. Ingresar una cantidad entera positiva que no supere los cupos y pulsar
   **Completar datos**. Se pueden agregar o quitar visitantes con los controles
   del formulario, respetando la disponibilidad.
4. Completar nombre, DNI de 7 u 8 dígitos, edad en años enteros y talle cuando
   corresponda a Tirolesa o Palestra.
5. Ingresar el email del titular y aceptar los términos específicos de la actividad.
6. Pulsar **Inscribirme**. Ante un rechazo, revisar el mensaje y corregir los datos.
7. Una inscripción aceptada lleva al cartel de confirmación y los QR por
   participante. **Ver mail** abre el correo simulado; sus adjuntos permiten
   descargar una tarjeta PNG con QR, datos del visitante, actividad y turno.

El correo es simulado: no llegará un mensaje a una bandeja real. El número de orden se muestra en la confirmación y en el correo simulado.

### Por qué pueden no aparecer días o turnos

La aplicación usa la hora real de Argentina (UTC−03:00) y mantiene las reglas
vigentes del backend:

- Se permite reservar desde **24 horas hasta 15 minutos antes** del inicio,
  incluidos ambos límites. No significa que haya que reservar exactamente 24 horas antes.
- Los turnos empiezan cada hora entre **09:00 y 17:00**, inclusive.
- El parque está cerrado los **lunes**, el **1 de enero** y el **25 de diciembre**.

Por eso el selector solo ofrece hoy y/o mañana si tienen turnos habilitados.
Un domingo, cuando ya cerró la inscripción al último turno, puede no haber
ninguna opción: el lunes está cerrado y el martes queda fuera de la ventana.
El aviso de falta de turnos en ese caso es el comportamiento esperado.

### Estado de la aplicación y revisión manual

Las reservas, cupos consumidos y correos simulados pertenecen al proceso que
está ejecutando Flask. Se pierden al reiniciarlo. No hay que crear una base de
datos ni ejecutar los antiguos scripts SQLite.

Para revisar la web, probar una inscripción individual y otra grupal, los
campos obligatorios, el límite de cupos, las edades mínimas, el rechazo por
superposición de DNI, la aceptación de términos y la visualización/descarga
de los QR y del correo simulado.

## Problemas frecuentes al ejecutar el frontend

| Problema | Qué revisar |
| --- | --- |
| `No module named ecoharmony` | Ejecutar la instalación editable de `backend[dev,web]` con el Python de `.venv`. |
| `No module named flask` | Instalar el extra `[web]` usando los comandos anteriores. |
| `Failed to find Flask application` o error de importación relativa | Ejecutar desde `Desarrollo/` y usar el nombre completo `frontend.eco_harmony_app.app`. No ejecutar `app.py` directamente. |
| Puerto ocupado o respuesta 403 en el puerto 5000 | Usar `--port 5001`; si también está ocupado, elegir otro puerto y abrir esa misma dirección. |
| El navegador no conecta | Comprobar que la terminal siga ejecutando Flask y que la URL coincida con el puerto anunciado. |
| No hay fechas o turnos | Revisar las reglas de anticipación, calendario y hora real explicadas arriba. |
| Se sigue viendo una pantalla anterior | Reiniciar Flask si no está en modo debug y recargar el navegador; para CSS/JS, usar recarga forzada. |
| Las reservas desaparecieron | El estado es en memoria y se reinicia con el servidor. |
| No llega el email | El envío es simulado: consultar **Ver mail** en la confirmación. |

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

### Instalación y pruebas

Seguir la sección **Configuración inicial: backend y frontend** de este README.
Para trabajar únicamente con el dominio, se puede instalar `backend[dev]`;
para ejecutar la web, usar `backend[dev,web]`.

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

Los comandos completos para Windows y macOS/Linux están en
**Configuración inicial: backend y frontend**. El frontend y el backend
comparten el mismo entorno virtual y se levantan con un único comando Flask.

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

### Datos entregados a las plantillas Jinja

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
  `actividad`, `turno` (texto legible en español) y `email`. El identificador
  de orden se muestra al visitante en la confirmación y en el correo simulado.
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
cuando el turno sigue disponible. La confirmación muestra los QR de los participantes
y acceso al contenido del único correo simulado mediante **Ver mail**. No se envían
emails a una bandeja real.

Verificación manual en navegador local: cantidad 11 frente a 10 cupos bloqueada;
reserva correcta con QR y correo simulado; nueva consulta con 9 cupos y cantidad 10
bloqueada; nombre vacío impide enviar; intento con DNI ya reservado en el mismo
turno rechazado con datos conservados. Queda por ampliar la revisión
visual en distintos tamaños de pantalla para la entrega final.

### Estado, reloj y límites

- Reservas, cupos, números de orden y correos simulados desaparecen al reiniciar.
- El reloj real se suministra desde Flask en UTC−03:00; no se cambia el dominio.
- Un bloqueo local serializa consultas y registros del adaptador en un proceso.
  No usar varios procesos/workers esperando compartir este estado en memoria.
- No se envían correos reales ni hay pagos o importes.
- Los términos por actividad se cargan desde `frontend/eco_harmony_app/terminos.json`,
  transcritos de «Propuesta de Logo y Términos y Condiciones» del equipo.
  Siguen siendo provisionales, pendientes de validación docente. Las condiciones
  informativas del documento no incorporan validaciones nuevas al backend.
