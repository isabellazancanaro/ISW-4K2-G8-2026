---
tags:
  - clase
  - isw
materia: ISW
fecha: 2026-09-04
---
# Proceso de Software
Conjunto estructurado (porque tienen orden y forma) de actividades para desarrollar un sistema de SW. 
Estas actividades dependen de la organizacion y del SW a construir.

La manera de instanciarlo es a traves de **proyectos**. El proceso es <u>abstracto</u>. -> Las actividades definidas en el proceso se ejecutan durante el proyecto.
![[Pasted image 20260904155737.png|359]]
Herramientas case, de despliegue automatizado, etc. -> permiten automatizar un proyecto.
Las **personas** son las que permiten llevar a cabo un proceso.
## Procesos definidos
Se asume que podemos **repetir** el proceso (idénticas tareas) para obtener el mismo resultado. Como si fuera predecible.
NO ES = entradas, = salidas.
<u>Predecibilidad a partir de la repetibilidad</u>.

Se implementaron, y con el tiempo surgieron algunas dificultades, de ahi surgen:
## Procesos empíricos
<u>Aprender a partir de la experiencia. </u>
![[Pasted image 20260904161055.png|329]]
(Ver diferencia entre retroalimentar y revisar).

NO ES la ausencia de un proceso. Son procesos menos prescriptivos en su definicion, dejan lugar para su adaptacion.
Un ejemplo es SCRUM. Hay un marco, y sobre el mismo voy aprendiendo. 

La necesidad del empirismo surge por los entornos de SW (cambiantes). 
### Ciclos de vida
**Del producto** -> Tiene que ver con el producto en si mismo. Inicia con la idea inicial y el concepto de MVP y termina cuando el producto deja de ser util porque fue reemplazado por ejemplo.

**Del proyecto** -> empieza cuando el proyecto inicia y cuando termina. 
- Tienen una duracion limitada. 
- Es algo unico. 
- Tienen un objetivo medible para decir cuando termina.
- Nos dice como se van a ejecutar las actividades propias del proceso.
- Es la representación del mismo. 
- Defino los modelos, las fases, como se van a ejecutar, en que orden, etc.
#### Tipos de ciclo de vida de proyecto:
- Secuencial
- Iterativo -> avanza. Luego de cada iteracion tenes un entregable.
- Recursivo -> vuelve sobre si mismo. 
Los procesos empiricos trabajan en un ciclo de vida iterativo. Los definidos en secuencial.
DEPENDE MUCHO DEL TIPO DE SW A FORMAR.
## Que es un proyecto?
### Características
- Son únicos. No hay dos iguales asi el "objetivo" sea "parecido".
- Tienen que tener una duracion limitada. Cuando empieza tengo que definir cual es el objetivo -> cuando termina
- Tiene que tener un objetivo. Medible y no ambiguo
- Tienen tareas interrelacionadas entre si, basadas en esfuerzos y recursos. Complejidad creciente.
## Planificación de proyectos
¿Por que es necesario tener un plan? -> Por la complejidad de las variables. Mientras mas grande sea el proyecto, mas dificil es de gestionar.
### Esencia vs Accidente
las ganancias en productividad vinieron de eliminar barreras artificiales.
Lo de las balas de plata vienen de eliminar esas **barreras accidentales** del SW. Problemas "Menores".
La parte **esencial** son problemas incurables. Problemas inherentes del SW. 
- Complejidad
- Conformidad
- Mutabilidad
- Invisibilidad
<u>Siempre se atacan los problemas accidentales, no los esenciales.</u>

Los hombres y los meses no son recursos intercambiables. Por mas que agregues gente, el proyecto no se va a hacer mas rapido. Es mas, se hace mas lento. 

Concepto de integridad conceptual y ecosistema del desarrollo.
## Administración de proyectos
TENER EL TRABAJO HECHO, en tiempo, con el presupuesto acordado y habiendo satisfecho las especificaciones o requerimientos. Una de las herramientas es la estimación.
### La triple restricción
- objetivos
- tiempo
- costos
El balance de los tres afecta directamente la calidad del proyecto. 
![[Pasted image 20260904164158.png]]
Cuando una de las variables se mueve, voy a tener que mover las otras si o si.
Eso es parte del trabajo del líder de proyecto.
### Rol del líder de proyecto
Es el que interactúa con el equipo y con todos los stakeholders. 
#### Equipo de proyecto
Grupo de personas comprometidas en alcanzar un conjunto de objetivos de los cuales se sienten mutuamente responsables.
##### Características
- Diversos conocimientos y habilidades
- posibilidad de desarrollar sinergia
- usualmente es un grupo pequeño
- tienen sentido de responsabilidad como una unidad
## Que es el plan de proyecto?
Es como la hoja de ruta de un viaje.
Documenta:
- Que hacemos?
- Cuando?
- Como?
- Quien?
### Disciplinas
- Definición del Alcance del Proyecto -> saber que trabajo tenemos que hacer para entregar el producto de SW en el contexto del proyecto.
	- Se mide contra el plan de proyecto. 
- Definición de proceso y ciclo de vida -> Si usamos un proceso definido o empírico y el ciclo de vida a utilizar.
	- Si es empírico probablemente no tengamos un PLAN como tal asi definido. 
- Estimación de SW
	- En proyectos definidos -> Tamaño, esfuerzo, calendario, costo, recursos críticos. En ese orden. 
- Gestión de Riesgos -> eventos que podría comprometer el éxito del proyecto. Siempre es una lista larga.
	- El riesgo tiene la variable del impacto y la de la probabilidad de ocurrencia.
	- Cuantos gestionamos depende del proyecto. Si estamos invirtiendo mas, gestionamos mas.
	- La lista se va actualizando. Los riesgos pueden tener un impacto hoy y otro distinto en el futuro. 
	- Riesgos tipicos
		- Dependencia de proveedores externos
		- Identificar mas las necesidades del cliente. -> no se le puede disminuir el impacto, si la probabilidad de ocurrencia.
		- hay mas.
- Asignación de recursos
- Programacion de proyectos
- Definición de controles
- Definición de métricas -> se dividen en: (en función de que miden)
	- de proceso
	- de proyecto -> miden lo que pasa en el proyecto y se supone que tienen una acción correctiva.
		- esfuerzo
		- tiempo
	- de producto -> tienen que ver con el producto de SW que yo construí
		- tamaño de producto
		- defectos
	- Las métricas de proyecto y proceso están relacionadas. Las métricas de proceso son las mismas que las de proyecto enunciadas de distinta manera. 