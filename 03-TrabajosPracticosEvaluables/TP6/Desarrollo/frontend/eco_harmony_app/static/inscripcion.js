"use strict";
const { talles: TALLES, valores } = JSON.parse(document.getElementById("datos-formulario").textContent);
const actividad = document.getElementById("actividad");
const dia = document.getElementById("dia");
const hora = document.getElementById("hora");
const cantidad = document.getElementById("cantidad");
const aviso = document.getElementById("aviso-hora");
const avisoCantidad = document.getElementById("aviso-cantidad");
const btnCompletar = document.getElementById("btn-completar");
const contenedor = document.getElementById("visitantes");
const final = document.getElementById("bloque-final");
const email = document.getElementById("email");
const terminos = document.getElementById("terminos");
const btnTerminos = document.getElementById("btn-terminos");
const panelTerminos = document.getElementById("terminos-panel");
let versionConsulta = 0;

// Conserva las restricciones HTML, pero reemplaza las burbujas del navegador.
const formulario = document.querySelector("form");
const erroresCampo = new WeakMap();
let numeroError = 0;
let focoPendiente = false;

function mensajeCampo(input) {
  if (input.validity.valid || input.disabled) return "";
  switch (input.name) {
    case "nombre": return "Ingresá el nombre del visitante.";
    case "dni": return "Ingresá un DNI de 7 u 8 dígitos numéricos.";
    case "edad":
      if (input.validity.valueMissing) return "Ingresá la edad del visitante.";
      if (input.validity.rangeUnderflow) return `La edad mínima para esta actividad es de ${input.min} años.`;
      return "Ingresá la edad en años cumplidos, sin decimales.";
    case "talle": return "Seleccioná el talle de vestimenta.";
    case "email": return "Ingresá un email válido para el titular.";
    case "terminos": return "Aceptá los términos y condiciones de la actividad para continuar.";
    case "actividad": return "Seleccioná una actividad.";
    case "turno": return "Seleccioná un horario disponible.";
    case "cantidad": return `Ingresá una cantidad entera entre 1 y ${cupos()}.`;
    default: return "Completá este campo para continuar.";
  }
}

function mostrarErrorCampo(input) {
  const mensaje = mensajeCampo(input);
  let error = erroresCampo.get(input);
  if (!error && mensaje) {
    error = document.createElement("p");
    error.id = `error-campo-${++numeroError}`;
    error.className = "error-campo";
    error.setAttribute("aria-live", "polite");
    const label = input.closest("label");
    (label || input).insertAdjacentElement("afterend", error);
    input.setAttribute("aria-describedby", [input.getAttribute("aria-describedby"), error.id].filter(Boolean).join(" "));
    erroresCampo.set(input, error);
  }
  if (error) {
    error.textContent = mensaje;
    error.hidden = !mensaje;
  }
  input.setAttribute("aria-invalid", String(Boolean(mensaje)));
}

formulario.addEventListener("invalid", e => {
  e.preventDefault();
  mostrarErrorCampo(e.target);
  if (!focoPendiente) {
    focoPendiente = true;
    queueMicrotask(() => {
      formulario.querySelector("input:invalid, select:invalid")?.focus();
      focoPendiente = false;
    });
  }
}, true);
formulario.addEventListener("focusout", e => {
  if (contenedor.contains(e.target) && e.target.matches("input, select")) mostrarErrorCampo(e.target);
});
for (const evento of ["input", "change"]) {
  formulario.addEventListener(evento, e => {
    if (erroresCampo.has(e.target)) mostrarErrorCampo(e.target);
  });
}

function ocultarTerminos() {
  panelTerminos.hidden = true;
  btnTerminos.setAttribute("aria-expanded", "false");
}
btnTerminos.addEventListener("click", () => {
  panelTerminos.hidden = !panelTerminos.hidden;
  btnTerminos.setAttribute("aria-expanded", String(!panelTerminos.hidden));
});
for (const id of ["cerrar-x", "cerrar-terminos"]) {
  document.getElementById(id).addEventListener("click", ocultarTerminos);
}
document.addEventListener("keydown", (e) => {
  if (e.key === "Escape") ocultarTerminos();
});
function actualizarTerminos() {
  document.getElementById("terminos-texto").textContent = actividad.selectedOptions[0]?.dataset.terminos || "";
  terminos.checked = false;
  ocultarTerminos();
}
function cupos() {
  return Number(hora.selectedOptions[0]?.dataset.disponibles || 0);
}
function validarCantidad() {
  cantidad.setCustomValidity("");
  const n = Number(cantidad.value);
  const valido = !cantidad.disabled && Number.isInteger(n) && n > 0 && n <= cupos();
  const mensaje = !cantidad.disabled && !valido
    ? `Ingresá una cantidad entera entre 1 y ${cupos()}.` : "";
  cantidad.setCustomValidity(mensaje);
  avisoCantidad.textContent = !cantidad.disabled && n > cupos()
    ? `Podés inscribir hasta ${cupos()} visitantes en este turno.`
    : !cantidad.disabled && !valido && contenedor.children.length > 0
      ? "Ingresá una cantidad válida de visitantes para continuar completando sus datos."
      : "";
  btnCompletar.disabled = !valido;
  return valido;
}
function leerVisitantes() {
  const datos = {};
  for (const nombre of ["nombre", "dni", "edad", "talle"]) {
    datos[nombre] = Array.from(contenedor.querySelectorAll(`[name="${nombre}"]`), input => input.value);
  }
  return datos;
}
function campo(etiqueta, nombre, valor = "") {
  const div = document.createElement("div");
  const label = document.createElement("label");
  label.textContent = etiqueta;
  const input = document.createElement("input");
  input.name = nombre;
  input.required = true;
  input.type = nombre === "edad" ? "number" : "text";
  if (nombre === "nombre") {
    input.pattern = ".*\\S.*";
    input.title = "Ingresá el nombre del visitante";
    input.autocomplete = "name";
  }
  if (nombre === "dni") {
    input.inputMode = "numeric";
    input.pattern = "[0-9]{7,8}";
    input.maxLength = 8;
    input.title = "Ingresá un DNI de 7 u 8 dígitos";
  }
  if (nombre === "edad") {
    input.min = actividad.selectedOptions[0].dataset.edadMinima;
    input.step = "1";
  }
  input.value = valor;
  label.append(input);
  div.append(label);
  return div;
}
function mostrarVisitantes(datos = leerVisitantes()) {
  if (!validarCantidad()) return;
  const n = Number(cantidad.value);
  contenedor.replaceChildren();
  for (let i = 0; i < n; i++) {
    const grupo = document.createElement("fieldset");
    const leyenda = document.createElement("legend");
    leyenda.textContent = `Visitante ${i + 1}`;
    grupo.append(leyenda);
    for (const [nombre, etiqueta] of [["nombre", "Nombre"], ["dni", "DNI"], ["edad", "Edad (años cumplidos)"]]) {
      grupo.append(campo(etiqueta, nombre, datos[nombre]?.[i] || ""));
    }
    if (actividad.selectedOptions[0].dataset.vestimenta === "1") {
      const label = document.createElement("label");
      label.textContent = "Talle de vestimenta";
      const select = document.createElement("select");
      select.name = "talle";
      select.required = true;
      select.add(new Option("-- Talle --", ""));
      for (const talle of TALLES) select.add(new Option(talle, talle));
      select.value = datos.talle?.[i] || "";
      label.append(select);
      grupo.append(label);
    }
    contenedor.append(grupo);
  }
  final.disabled = false;
}
btnCompletar.addEventListener("click", () => mostrarVisitantes());
cantidad.addEventListener("input", () => {
  final.disabled = true;
  const valido = validarCantidad();
  for (const grupo of contenedor.children) grupo.disabled = !valido;
});
function seleccionarTurno() {
  contenedor.replaceChildren();
  final.disabled = true;
  const disponibles = cupos();
  cantidad.disabled = disponibles < 1;
  cantidad.max = String(disponibles);
  validarCantidad();
}
hora.addEventListener("change", seleccionarTurno);
async function cargarHoras(turnoAnterior = "") {
  const version = ++versionConsulta;
  hora.replaceChildren(new Option("-- Seleccioná un horario --", ""));
  hora.disabled = true;
  seleccionarTurno();
  aviso.textContent = "";
  if (!actividad.value || !dia.value) return;
  const params = new URLSearchParams({ actividad: actividad.value, fecha: dia.value });
  try {
    const respuesta = await fetch("/api/horarios?" + params);
    if (!respuesta.ok) throw new Error();
    const horarios = await respuesta.json();
    if (version !== versionConsulta) return;
    if (!horarios.length) aviso.textContent = "No hay horarios disponibles ese día.";
    for (const h of horarios) {
      const opcion = new Option(`${h.texto} · ${h.disponibles > 0 ? `quedan ${h.disponibles}` : "completo"}`, h.valor);
      opcion.dataset.disponibles = String(h.disponibles);
      opcion.disabled = h.disponibles < 1;
      hora.add(opcion);
    }
    hora.disabled = horarios.length === 0;
    if (turnoAnterior && horarios.some(h => h.valor === turnoAnterior && h.disponibles > 0)) {
      hora.value = turnoAnterior;
      seleccionarTurno();
    }
  } catch {
    if (version === versionConsulta) aviso.textContent = "No se pudieron cargar los horarios. Probá de nuevo.";
  }
}
actividad.addEventListener("change", () => {
  dia.disabled = !actividad.value || dia.options.length < 2;
  actualizarTerminos();
  cargarHoras();
});
dia.addEventListener("change", () => cargarHoras());
document.querySelector("form").addEventListener("submit", e => {
  if (!validarCantidad() || final.disabled || contenedor.children.length !== Number(cantidad.value)) {
    e.preventDefault();
    avisoCantidad.textContent = "Elegí una cantidad válida y completá los datos de los visitantes antes de confirmar.";
  }
});
async function restaurar() {
  actividad.value = valores.actividad?.[0] || "";
  dia.disabled = !actividad.value || dia.options.length < 2;
  actualizarTerminos();
  email.value = valores.email?.[0] || "";
  cantidad.value = valores.cantidad?.[0] || "";
  const turno = valores.turno?.[0] || "";
  dia.value = turno.slice(0, 10);
  await cargarHoras(turno.slice(0, 16));
  if (hora.value && validarCantidad()) {
    mostrarVisitantes(valores);
    terminos.checked = valores.terminos?.[0] === "1";
  }
  document.getElementById("error-servidor")?.focus();
}
restaurar();
