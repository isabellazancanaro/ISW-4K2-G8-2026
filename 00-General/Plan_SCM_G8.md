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
├── 01-Bibliografía/
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
| Plan SCM | Proyecto | Plan_SCM_G8.md | 00-General/ |
| Programa Asignatura | Proyecto | Programa_Asignatura.pdf | 00-General/ |
| Pautas de Email | Proyecto | Pautas_Email.pdf | 00-General/ |
| Bibliografía | Referencia | [Nombre].pdf | 01-Bibliografía/[Tema]/ |
| Presentaciones de Clase | Referencia | [Numero]_[Tema].pdf | 02-PresentacionesClases/ |
| Consigna TP Evaluable | Iteración | Consigna_TP[Numero].pdf | 03-TrabajosPracticosEvaluables/TP[Numero]/ |
| Entrega TP Evaluable | Iteración | TP[Numero]_4K2_G8_2026.[ext] | 03-TrabajosPracticosEvaluables/TP[Numero]/Desarrollo/ |
| Consigna TIG | Iteración | Consigna_TIG[Numero].pdf | 04-TrabajosInvestigacion/TIG[Numero]/ |
| Entrega TIG | Iteración | TIG[Numero]_4K2_G8_2026.[ext] | 04-TrabajosInvestigacion/TIG[Numero]/ |
| Templates de Cátedra | Referencia | [NombreTemplate].[ext] | 05-Ejercicios/TemplatesYSoluciones/ |
| Soluciones de Cátedra | Referencia | Solucion_[Tema].[ext] | 05-Ejercicios/TemplatesYSoluciones/ |
| Ejercicios Prácticos de Alumnos | Soporte | Ejercicio_[Tema]_[NombreEjercicio].[ext] | 05-Ejercicios/Parcial[Numero]/[Apellido] |
| Resúmenes para Parcial | Soporte | Resumen_[Apellido].[ext] | 06-Estudio/Parcial[Numero]/Resumenes/ |
| Notas y Apuntes de Clase | Soporte | Notas_[DDMM]_[Tema]_[Apellido].[ext] | 06-Estudio/Parcial[Numero]/NotasClase/ |


## Glosario
- ISW -> Ingeniería y Calidad de Software
- G8 -> Grupo 8
- TP -> Trabajo Práctico
- TIG -> Trabajo de Investigación Grupal
- DDMM -> Fecha en formato Dia/Mes
- ext -> Extensión o formato del ítem de configuración
- [Apellido] -> Apellido del alumno autor del archivo
- IC -> Ítem de Configuración

## Criterio de línea base
Como grupo definimos establecer una línea base al momento de la entrega de un Trabajo Práctico Evaluable o un Trabajo de Investigación Grupal. 

Un item de configuración sera considerado parte de la linea base cuando:
- Haya pasado por la revisión de 2 miembros del grupo.
- Esté completo y en su versión definitiva.   
- Se ajuste al formato y la ubicación establecidos en el listado de ítems de configuración.

Para la creación de la linea base se usaran etiquetas de la herramienta de versionado Git, las cuales se nombrarán con el formato "tp[N]-entrega" o "tig[N]-entrega", en función de lo entregado.
En caso de necesitar hacer una corrección sobre una entrega, se creará otra linea base, agregando al nombre la version "tp[N]-entrega-v[N]".