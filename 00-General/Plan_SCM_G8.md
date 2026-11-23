# ISW-G8-2026

Repositorio del Grupo 8 - Ingeniería y Calidad de Software - 4K2 - 2026

## Integrantes
- 401919 - Allasia, Luciano
- 403938 - Bertuzzi, Valentin
- 402494 - Maggi, Geronimo 
- 401156 - Mamud, Savina
- 400809 - Mandrile, Virginia Maria
- 400483 - Piscitello, Tomas 
- 400299 - Ritta, Guillermina 
- 400653 - Ruiz, Juan Jose
- 87979  - Salguero, Mateo
- 400430 - Suárez, Florencia
- 400181 - Talone, Álvaro
- 403862 - Zancanaro, Isabella 

## Estructura del Repositorio
```
ISW-G8-2026/
├── 00-General/
├── 01-Bibliografia/
│   ├── IngenieriaDeSoftware/
│   ├── SCM/
│   ├── TestingDeSoftware/
│   ├── TDD/
│   ├── Agilismo/
│   └── LeanYKanban/
├── 02-PresentacionesClases/
├── 03-TrabajosPracticosEvaluables/
│   └── TP[Número]/
│       └── Desarrollo/
├── 04-TrabajosInvestigacion/
│   ├── TIG1/
│   └── TIG2/
├── 05-Ejercicios/
│   ├── TemplatesYSoluciones/
│   ├── Parcial1/
|   |   └── [Apellido]/
│   └── Parcial2/
|       └── [Apellido]/
└── 06-Estudio/
    ├── Parcial1/
    │   ├── Resumenes/
    │   └── NotasClase/
    └── Parcial2/
        ├── Resumenes/
        └── NotasClase/
```

## Reglas de nombrado

### Convenciones generales de formato
- Carpetas: PascalCase
- Archivos: Snake_Case_Con_Mayusculas

| Ítem de Configuración | Tipo IC | Regla de Nombrado | Ubicación en el Repositorio |
| :--- | :--- | :--- | :--- |
| Plan SCM  | Gestión | Plan_SCM_G8.md | 00-General/ |
| Programa Asignatura | Gestión | Programa_Asignatura.pdf | 00-General/ |
| Pautas de Email | Gestión | Pautas_Email.pdf | 00-General/ |
| Cronograma Asignatura | Gestión | Cronograma_Asignatura.pdf | 00-General/ |
| Bibliografía | Referencia | [Nombre].pdf | 01-Bibliografia/[Tema]/ |
| Presentaciones de Clase | Referencia | [Numero]_[Tema].pdf | 02-PresentacionesClases/ |
| Enunciados TPs Evaluables | Referencia | Enunciados_TP_Evaluables_2026_2do_Cuatrimestre.pdf | 03-TrabajosPracticosEvaluables/ |
| Consigna TP Evaluable | Referencia | Consigna_TP[Numero].pdf | 03-TrabajosPracticosEvaluables/TP[Numero]/ |
| Entrega TP Evaluable | Entregable | TP[Numero]_4K2_G8_2026.[ext] | 03-TrabajosPracticosEvaluables/TP[Numero]/Desarrollo/ |
| Código Fuente TP Evaluable | Entregable | backend/, frontend/eco_harmony_app/, .gitignore, README.md | 03-TrabajosPracticosEvaluables/TP[Numero]/Desarrollo/ |
| Lineamientos TIG | Referencia | Lineamientos_Para_Trabajos_De_Investigacion_2026_2C.pdf | 04-TrabajosInvestigacion/ |
| Entrega TIG | Entregable | TIG[Numero]_4K2_G8_2026.[ext] | 04-TrabajosInvestigacion/TIG[Numero]/ |
| Templates de Cátedra | Referencia | [NombreTemplate].[ext] | 05-Ejercicios/TemplatesYSoluciones/ |
| Guía de Trabajos Prácticos Resueltos | Referencia | ISW_Guia_De_Trabajos_Practicos_Resueltos.docx.pdf | 05-Ejercicios/TemplatesYSoluciones/ |
| Ejercicios Prácticos de Alumnos | Soporte | Ejercicio_[Tema]_[NombreEjercicio].[ext] | 05-Ejercicios/Parcial[Numero]/[Apellido] |
| Resúmenes para Parcial | Soporte | Resumen_[Apellido].[ext] | 06-Estudio/Parcial[Numero]/Resumenes/ |
| Notas y Apuntes de Clase | Soporte | Notas_[DD-MM]_[Tema]_[Apellido].[ext] | 06-Estudio/Parcial[Numero]/NotasClase/ |


## Glosario
- ISW -> Ingeniería y Calidad de Software
- G8 -> Grupo 8
- TP -> Trabajo Práctico
- TIG -> Trabajo de Investigación Grupal
- DD-MM -> Fecha en formato Dia/Mes
- ext -> Extensión o formato del ítem de configuración
- [Apellido] -> Apellido del alumno autor del archivo
- IC -> Ítem de Configuración
- Tipo IC -> Gestión (organiza la cursada), Referencia (material de cátedra), Entregable (producido y entregado por el grupo), Soporte (material de estudio individual)

## Criterio de línea base
Como grupo definimos establecer una línea base al momento de la entrega de un Trabajo Práctico Evaluable o un Trabajo de Investigación Grupal. 

Un item de configuración será considerado parte de la línea base cuando:
- Ha pasado por la revisión de 2 miembros del grupo.
- Esté completo y en su versión definitiva.   
- Se ajusta al formato y la ubicación establecidos en el listado de ítems de configuración.

Para la creación de la línea base se usarán etiquetas de la herramienta de versionado Git, las cuales se nombran con el formato "tp[N]-entrega" o 
"tig[N]-entrega", en función de lo entregado.

En caso de necesitar hacer una corrección sobre una entrega, se creará otra línea base, agregando al nombre la versión "tp[N]-entrega-v[N]".
