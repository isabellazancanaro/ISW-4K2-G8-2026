# EcoHarmony Park – TP6 TDD · Instrucciones para correr el proyecto

User Story implementada: **«Inscribirme a actividad»** (grupo par).
Backend en Python (POO + funciones puras) desarrollado con TDD y pytest; interfaz web responsive en Flask + Jinja2 + JavaScript.

## Requisitos

- **Python 3.12 o superior** (`python --version`)
- **Git**
- Conexión a internet (para instalar dependencias y cargar la tipografía Lato desde Google Fonts)

## 1. Clonar el repositorio

```bash
git clone https://github.com/isabellazancanaro/ISW-4K2-G8-2026.git
cd ISW-4K2-G8-2026/03-TrabajosPracticosEvaluables/TP6/Desarrollo
```

Se trabaja sobre la rama `main`, que contiene todo el desarrollo integrado. Todos los comandos siguientes se ejecutan **desde la carpeta `Desarrollo/`**, salvo que se indique otra cosa.

## 2. Crear y activar el entorno virtual

**Windows (PowerShell):**
```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```
Si PowerShell bloquea el script de activación: `Set-ExecutionPolicy -Scope Process Bypass` y volver a activar.

**Linux / macOS:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

## 3. Instalar dependencias

Primero el backend (instala el paquete `ecoharmony` en modo editable, con las dependencias de pruebas):

```powershell
python -m pip install -e ".\backend[dev]"
```
En Linux / macOS: `python -m pip install -e "./backend[dev]"`

Después las dependencias de la web:

```bash
python -m pip install -r frontend/eco_harmony_app/requirements.txt
```

## 4. Ejecutar las pruebas automatizadas (backend)

```bash
python -m pytest -v backend/tests
```

Resultado esperado: **todas las pruebas en verde** (`98 passed` en la última verificación; los escenarios con varios casos están parametrizados, por eso hay más pruebas que escenarios). Cada prueba lleva en su nombre el ID del escenario (`test_cup_01_…`, `test_tal_08_…`, etc.).

## 5. Levantar la aplicación web

```bash
cd frontend
python -m flask --app eco_harmony_app.app run --debug
```

Abrir en el navegador: **http://127.0.0.1:5000**

Si el puerto 5000 está ocupado, agregar `--port 5001` y abrir esa dirección. Para detener el servidor: `Ctrl + C`.

> Los datos (inscripciones, cupos y correos simulados) **se guardan en memoria**: se pierden al reiniciar el servidor. Es una decisión del grupo (sin base de datos).

## 6. Recorrido sugerido para probar la web

1. En el inicio, **Inscribirme a actividad**.
2. Elegir actividad, día y horario (cada horario muestra los cupos que quedan).
3. Indicar la cantidad de visitantes y **Completar datos**. Con **+ Agregar visitante** se suma otro; con la ✕ de cada card se quita.
4. Completar nombre, DNI (7 u 8 dígitos), edad y, en Tirolesa y Palestra, el talle.
5. Ingresar el email del titular, aceptar los términos de la actividad e **Inscribirme**.
6. En la pantalla final: número de orden, turno, visitantes y **Ver mail** (correo simulado con un QR por participante). Los adjuntos del mail descargan un PNG con el QR, los datos del visitante, la actividad y el turno.

Casos de rechazo para probar: no aceptar los términos, edad menor a la mínima (Tirolesa 8, Palestra 12), pedir más personas que los cupos disponibles, repetir un DNI ya inscripto en otra actividad del mismo horario, y Safari / Jardinería con talle informado (no admiten talle).

## 7. Importante: qué turnos se pueden elegir (reloj real)

Las reglas del enunciado hacen que la web solo ofrezca turnos **desde 24 horas hasta 15 minutos antes de su inicio**, con horarios en punto de 09:00 a 17:00. El parque está cerrado los **lunes**, el **25/12** y el **1/1**. Por eso el selector de día solo muestra «Hoy» y/o «Mañana», y puede aparecer el aviso *«No hay días con turnos disponibles en este momento»* (por ejemplo, un domingo a la noche, porque el lunes está cerrado y hoy ya no quedan turnos).

Si al probar no aparecen turnos, levantar la app con un **reloj fijo** (martes 20/10/2026 a las 08:00, hora de Argentina) desde `Desarrollo/frontend`:

```bash
python -c "from datetime import datetime; from eco_harmony_app.app import crear_app, ZONA; crear_app({'RELOJ': lambda: datetime(2026, 10, 20, 8, 0, tzinfo=ZONA)}).run(debug=False)"
```

Con ese reloj aparece «Hoy · martes 20/10» con turnos de 09:00 a 17:00.

## 8. Historial TDD

Los commits conservan el ciclo Red-Green-Refactor (sin squash):

```bash
git log --oneline --graph
```

Prefijos: `test(red): …`, `feat(green): …`, `refactor: …`.

## Estructura del proyecto

```
Desarrollo/
├── backend/
│   ├── pyproject.toml
│   ├── src/ecoharmony/        # dominio: reglas de negocio, modelos (models/), servicios
│   └── tests/                 # pruebas pytest del backend
└── frontend/
    └── eco_harmony_app/       # Flask: app.py, horarios.py, templates/, static/
```

La web **no duplica reglas de negocio**: `app.py` solo adapta el formulario HTTP y delega todas las validaciones en `ServicioInscripciones` del backend.

## Problemas frecuentes

| Síntoma | Solución |
|---|---|
| `ModuleNotFoundError: ecoharmony` | Falta el paso 3 o el entorno virtual no está activado. Reinstalar con `python -m pip install -e ".\backend[dev]"`. |
| `No module named flask` / `qrcode` / `zxingcpp` | `python -m pip install flask "qrcode[pil]" zxing-cpp` |
| `Failed to find Flask application` / `attempted relative import` | Ejecutar el comando del paso 5 **desde `Desarrollo/frontend`** y con `--app eco_harmony_app.app`. |
| La página no tiene estilos o tipografía | La tipografía Lato se descarga de Google Fonts: requiere internet. |

## Notas del alcance

- Actividades gratuitas: no hay precios ni importes.
- Los textos de términos y condiciones son **provisorios** hasta su validación docente.
- El correo es **simulado** (no se envían emails reales); los códigos QR son genuinos y legibles con cualquier lector.
- La justificación de las decisiones de diseño se entrega en el documento externo.