# EcoHarmony Park — TP6

## Paso a paso para abrir la web en una computadora nueva

### 1. Instalar los requisitos

- **Python 3.12 o superior:** [descargar Python](https://www.python.org/downloads/). En Windows, habilitar la opción de agregar Python al PATH durante la instalación.
- **Git:** [descargar Git](https://git-scm.com/downloads).
- Tener conexión a internet para descargar el proyecto y sus dependencias.

Abrir **PowerShell** en Windows o **Terminal** en macOS/Linux y comprobar:

```bash
git --version
```

Para comprobar Python, usar `py -3 --version` en Windows o `python3 --version`
en macOS/Linux. La versión debe ser 3.12 o superior.

### 2. Descargar el proyecto y entrar en la carpeta correcta

Desde la carpeta donde se quiera guardar el repositorio, ejecutar:

```bash
git clone --branch feature/tp6-sg4-tdd --single-branch https://github.com/isabellazancanaro/ISW-4K2-G8-2026.git
cd ISW-4K2-G8-2026/03-TrabajosPracticosEvaluables/TP6/Desarrollo
```

Los comandos siguientes se ejecutan desde **TP6/Desarrollo**, no desde la raíz
del repositorio ni desde la carpeta de otro trabajo práctico.

### 3. Preparar el entorno e iniciar la aplicación

Elegir los comandos correspondientes al sistema operativo. Se instala el
backend y el frontend en un mismo entorno; no hay que iniciar dos servidores.

**Windows — PowerShell:**

```powershell
py -3 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -e ".\backend[dev,web]"
.\.venv\Scripts\python.exe -m flask --app frontend.eco_harmony_app.app run --host 127.0.0.1 --port 5001
```

**macOS / Linux:**

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -e './backend[dev,web]'
.venv/bin/python -m flask --app frontend.eco_harmony_app.app run --host 127.0.0.1 --port 5001
```

No hace falta activar el entorno virtual, instalar Node.js ni crear una base
de datos. Los comandos utilizan directamente el Python de `.venv`.

### 4. Abrir la página

Cuando la terminal muestre `Running on http://127.0.0.1:5001`, abrir en el navegador:

**[http://127.0.0.1:5001](http://127.0.0.1:5001)**

Mantener la terminal abierta mientras se usa la web. En la página de inicio,
pulsar **Inscribirme a actividad**, elegir actividad y turno, completar los
visitantes, ingresar el email del titular y aceptar los términos. Al confirmar,
se muestran el número de orden, los QR y el botón **Ver mail**.

### 5. Detenerla o volver a abrirla

- Para detener el servidor, presionar **Ctrl+C** en la terminal.
- Para volver a abrirlo, entrar otra vez en `TP6/Desarrollo` y repetir únicamente
  el último comando del paso 3, el que ejecuta Flask.
- Si se cambian archivos Python o plantillas, reiniciar Flask para cargar los cambios.
- Las reservas y los correos simulados se pierden al reiniciar el servidor.

### Si algo no funciona

| Problema | Solución |
| --- | --- |
| No encuentra `.venv/bin/python` o `.venv\Scripts\python.exe` | Comprobar que se está en `TP6/Desarrollo` y crear el entorno con el paso 3. |
| No encuentra `flask` o `ecoharmony` | Repetir la instalación de `backend[dev,web]` del paso 3. |
| Puerto 5001 ocupado | Cambiar `--port 5001` por `--port 5002` y abrir `http://127.0.0.1:5002`. |
| El navegador no conecta | Revisar que Flask siga ejecutándose y que la dirección use el mismo puerto. |
| No aparecen días o turnos | Solo se puede reservar entre 24 horas y 15 minutos antes del turno. Los lunes, el 1 de enero y el 25 de diciembre el parque está cerrado. Los turnos comienzan de 09:00 a 17:00. Puede no haber opciones según la fecha y hora actuales. |
| No llega un email | El envío es simulado. El contenido se consulta mediante **Ver mail** en la confirmación. |

## Descripción del proyecto

Trabajo práctico de Ingeniería y Calidad de Software — UTN FRC, Grupo 8.
Implementa la historia de usuario **«Inscribirme a actividad»** de EcoHarmony Park.

Permite realizar inscripciones individuales y grupales a Tirolesa, Safari,
Palestra y Jardinería, consultar cupos y validar datos, edades, vestimenta,
términos y superposiciones. Una solicitud grupal se acepta o rechaza completa.
La confirmación incluye número de orden, un QR por participante y un correo
simulado al titular. Las actividades son gratuitas.

### Tecnologías y organización

Backend en Python con enfoque orientado a objetos y pruebas pytest. Frontend
responsive con Flask, Jinja2, HTML, CSS y JavaScript, usando la paleta del equipo,
la fuente Lato y el logo. Lato se descarga desde Google Fonts; sin conexión,
se utiliza la fuente alternativa definida en los estilos.

| Subgrupo | Aporte |
| --- | --- |
| 1 | Base del proyecto, catálogo de actividades, calendario, horarios, anticipación y disponibilidad. |
| 2 | Validaciones de nombre, DNI, edad, talles, términos y cantidad de participantes. |
| 3 | Inscripciones, consumo de cupos, superposiciones, estado, confirmaciones, QR y correo simulado. |
| 4 | Pantallas responsive, integración con el backend y verificación manual del flujo web. |

### Estructura

- `backend/src/ecoharmony/`: modelos, reglas de negocio y servicios.
- `backend/tests/`: pruebas automatizadas de los subgrupos de backend.
- `backend/pyproject.toml`: configuración y dependencias Python.
- `frontend/eco_harmony_app/app.py`: aplicación Flask y rutas.
- `frontend/eco_harmony_app/horarios.py`: opciones de turnos usando las reglas del backend.
- `frontend/eco_harmony_app/templates/`: pantallas de inicio, inscripción y confirmación.
- `frontend/eco_harmony_app/static/`: CSS, JavaScript y logo.
- `frontend/eco_harmony_app/terminos.json`: términos por actividad.
- `frontend/eco_harmony_app/requirements.txt`: dependencia Flask.

### Pruebas y metodología

El backend se desarrolló mediante ciclos **RED–GREEN–REFACTOR**, conservados en
el historial Git. Desde `Desarrollo`, ejecutar las 98 pruebas del backend:

**Windows:**

```powershell
.\.venv\Scripts\python.exe -m pytest -q backend/tests
```

**macOS / Linux:**

```bash
.venv/bin/python -m pytest -q backend/tests
```

El frontend se verifica manualmente desde el navegador.

### Alcance y límites

- El almacenamiento es en memoria y no sobrevive al reinicio del proceso.
- Los correos son simulados; los QR generados son reales y descargables.
- La configuración local utiliza un único proceso; no comparte reservas entre servidores.
- La justificación de decisiones de diseño se entrega en el documento externo del equipo.
