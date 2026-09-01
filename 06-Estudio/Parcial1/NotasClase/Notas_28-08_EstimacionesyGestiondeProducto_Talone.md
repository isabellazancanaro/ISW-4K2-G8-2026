---
tags:
  - clase
  - isw
materia: ISW
fecha: 2026-08-28
---
# Estimaciones de Software
### En contexto de la gestión tradicional de proyectos

**Concepto** -> predecir acerca del futuro a traves de una tecnica.
La tecnica no da como resultado la planificacion del proyecto. Me da un input (una base) para que lo haga. Para formular el plan tomamos como base la estimacion. NO SON COMPROMISOS.

Hay un cierto nivel de **incertidumbre** dependiendo del punto en que estemos del proyecto (al principio es mayor).
![[Pasted image 20260828154902.png|590]]
Sin embargo, una estimacion al final del proyecto no sirve de nada. Hay una estimación inicial y a partir de ahi se va refinando. 
El proceso de estimaciones **no es** **estático**. 

Se debe tratar de combinar distintas **tecnicas** de estimacion para achicar lo mas posible el error de calculo.
Los **errores** provienen de:
- no usar ninguna tecnica
- no combinar tecnicas
- no iterar sobre las estimaciones
## ¿Qué estimamos?
- Tiempo
- Esfuerzo -> hs lineales que me lleva hacer una act
- Tamaño
- Recursos
Estas son MEDIDAS ABSOLUTAS.
## Problemas al estimar
- Ser muy optimistas
- Actividades omitidas
## Técnicas de estimacion

### Contar
Es el método mas básico de estimación. Es contar cuanto me puede llevar algo. 
**Metodos**:
- **basados en la experiencia** -> necesito un experto. Son los que mas vamos a usar.
	- <u>datos historicos</u> -> recopilan datos historicos para hacer una estimacion a partir de los mismos. Problema -> A veces es dificil comparar los datos historicos. Como los tomo para que me sirvan para hacer la estimacion? Otra dificultad es guardarlos. 
	- <u>juicio experto</u> -> un experto estudia las especificaciones y hace su estimacion. Primer problema -> de donde saco el experto. Es el metodo mas utilizado. Surge el metodo "optimista, pesimista y habitual" con su formula, para estructurar la estimacion de juicio experto. 
		- <u>puro</u>
		- <u>delphi</u> -> tambien estructura el juicio experto. Tenemos un grupo de personas que hacen una estimacion grupal y que buscan llegar a un consenso. No es una democracia. A traves de las iteraciones se refina para llegar a un unico valor. Hay un coordinador que maneja las estimaciones de cada uno para que despues se itere sobre las mismas.
			![[Pasted image 20260828160215.png|533]]
	- <u>analogia</u> 
- **basados en los recursos**
- **basados en el mercado**
- **basados en los componentes del producto o en el proceso de desarrollo**
- **metodos algoritmicos**
# Estimaciones en ambientes Agiles

Las medidas son **RELATIVAS**. No como las mencionadas antes. 
Utilizamos **Story Points (SP)**. Solamente tiene sentido para el equipo de trabajo que trabaja con ella. 
## Estimaciones relativas
Se usan porque las personas no saben estimar en términos absolutos. Es mucho mas facil comparar.
### Trabajo VS Esfuerzo
Descripcion de la tarea VS lo que cuesta llevarla adelante. 
<u>El tamaño no es esfuerzo.</u> 

Usamos el termino **tamaño como medida relativa** para hacer las estimaciones en entornos agiles. 
Debemos definir una **ESCALA**. Una vez definida no cambia. 
### Story Point (SP)
Peso que le vamos a dar a cada historia. A partir del mismo es como la comparamos con otras. 
Le damos un **peso a las User** en el que vamos a tener en cuenta:
- complejidad
- esfuerzo
- duda / incertidumbre
![[Pasted image 20260828161726.png|388]]

Una de las unidades de medida mas utilizadas es la serie de fibonacci. Porque la complejidad de las US tiende a agrandarse exponencialmente. 
### Poker Estimation
La base es el Wideband Delphi. Combina juicio experto, analogia y desagregacion. 
Los expertos (quienes estiman) son los desarrolladores (quienes hacen las tareas).

Tomamos una **US CANONICA** -> suficientemente pequeña para asignarle el valor 1 de fibonacci. 
A partir de ahi, definimos:
![[Pasted image 20260828162139.png]]

<u>La base del empirismo es inspeccionar, adaptarse e iterar.</u> 


# Gestión de producto

El mayor riesgo al construir SW es hacer un producto que nadie va a utilizar. Crear mas SW y mas rapido NO IMPLICA DAR VALOR.
### ¿Qué es dar valor?
Ya no es solamente que satisfaga las necesidades. Entra tambien la experiencia de uso.
Lo VIABLE ya no es suficiente. Hay que hacer algo MEMORABLE. Tengo que hacer un producto que el usuario QUIERA utilizar. Por la competencia. 
## Ciclo Lean Startup
Cuando creamos un SW queremos poder evaluarlo, para poder modificar lo planteado inicialmente, y volver a construir. 
### Producto Minimo Viable (MVP)
Producto que el cliente percibe como real, a partir del cual valido si es lo que el cliente quiere o no. 
Es minimo producto viable porque lo que queremos es no tener desperdicio (features no usadas, etc.)
Se usa para tener feedback del cliente invirtiendo el minimo esfuerzo en construirlo hasta no saber que hay un interes genuino en el producto. 

Para construir un MVP hay que hacerlo con "fetas" verticales.![[Pasted image 20260828163518.png|428]]

Yo tengo una PROPUESTA DE VALOR UNICA (UVP) que es mi hipotesis inicial, y hago el MVP para probar esa hipotesis. 

La idea es que no sea un problema tener que hacer varios MVP hasta probar la hipotesis. 
### ¿Que va en un MVP?
- Componentes urgentes e importantes de funcionalidad
### MMF (Minimum Marketable Feature)
Ya es un release del producto. Minimo producto comercializable. 
## ¿Como escalamos un MVP?
![[Pasted image 20260828164324.png]]
A partir del MVP genero los releases agregando caracteristicas que den valor. 
## MLP (Minimum Lovable Product)
Surge por la competencia. Por que la gente deberia elegir tu producto. 