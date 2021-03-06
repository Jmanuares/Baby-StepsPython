                                                    TP1 – Introducción a Python
```diff
-Nota: La implementación también se debe documentar, con comentarios dentro y fuera del código, 
-al respecto de qué hace el programa, cómo lo hace y por qué lo hace de esa forma.
```
1. Escribir un programa que pregunte al usuario:
    1. Su nombre, y luego lo salude.
    2. Dos números, y luego muestre el producto.

2. Implementar algoritmos (en forma de función) que permitan:
    1. Calcular el perímetro de un rectángulo dada su base y su altura.
    2. Calcular el área de un rectángulo dada su base y su altura.
    3. Calcular el área de un rectángulo (alineado con los ejes x e y ) dadas sus coordenadas
    x1,x2, y1,y2.
    4. Calcular el perímetro de un círculo dado su radio.
    5. Calcular el área de un círculo dado su radio.
    6. Calcular el volumen de una esfera dado su radio.
    7. Dados los catetos de un triángulo rectángulo, calcular su hipotenusa.

3. Implementar un algoritmo (en una o más funciones) que, dado un número entero n, permita
calcular su factorial.

4. Escribir un programa (con al menos una función) que convierta un valor dado en grados
Fahrenheit a grados Celsius. Recordar que la fórmula para la conversión es: F = 9/5 C + 32.

5. Utilice el programa anterior para generar (imprimir en pantalla) una tabla de conversión de
temperaturas, desde 0 °F hasta 120 °F, de 10 en 10.
Nota: La forma ideal es haber implementado en el ejercicio anterior una función para
hacer la traducción entre Fahrenheit y Celcius. En este ejercicio, lo que resta es crear,
para este ejercicio, una función que llame a la anterior varias veces.

6. Escribir una función que, dados cuatro números, devuelva el mayor producto de dos de
ellos. Por ejemplo, si recibe los números 1, 5, -2, -4 debe devolver 8, que es el producto más
grande que se puede obtener entre ellos (8 = −2 × −4).

7. Escribir funciones que resuelvan los siguientes problemas:
    1. Dado un año indicar si es bisiesto. (Nota: un año es bisiesto si es un número divisible
    por 4, pero no si es divisible por 100, excepto que también sea divisible por 400).
    2. Dado un mes, devolver la cantidad de días correspondientes.
    3. Dada una fecha (día, mes, año), indicar si es válida o no.
    4. Dada una fecha, indicar los días que faltan hasta fin de mes.
    5. Dada una fecha, indicar los días que faltan hasta fin de año.
    6. Dada una fecha, indicar la cantidad de días transcurridos en ese año hasta esa fecha.
    7. Dadas dos fechas (día1, mes1, año1, día2, mes2, año2), indicar el tiempo transcurrido
    entre ambas, en años, meses y días.
    Nota: en todos los casos, invocar las funciones escritas previamente cuando sea posible.

8. (Puede ser difícil) Escribir un programa que reciba como entrada un entero representando un
año (por ejemplo 751, 1999, o 2158), y muestre por pantalla el mismo año escrito en
números romanos.

9. Escribir un programa que contenga una contraseña inventada, que le pregunte al usuario la
contraseña, y no le permita continuar hasta que la haya ingresado correctamente.
    1. Modificar el programa anterior para que solamente permita una cantidad fija de intentos.
    2. Modificar el programa anterior para que después de cada intento agregue una pausa cada
    vez mayor, utilizando la función sleep del módulo time.
    3. Modificar el programa anterior para que sea una función que devuelva si el usuario
    ingresó o no la contraseña correctamente, mediante un valor booleano (True o False).

10. Utilizando la función randrange del módulo random, escribir un programa que tenga un
número aleatorio secreto, y luego permita al usuario ingresar números y le indique si son
menores o mayores que el número a adivinar, hasta que el usuario ingrese el número
correcto.

11. Escribir una función que dada la cantidad de ejercicios de un examen, y el porcentaje
necesario de ejercicios bien resueltos necesario para aprobar dicho examen, revise un grupo
de exámenes. Para ello, en cada paso debe preguntar la cantidad de ejercicios resueltos por
el alumno, indicando con un valor centinela que no hay más exámenes a revisar. Debe
mostrar por pantalla el porcentaje correspondiente a la cantidad de ejercicios resueltos
respecto a la cantidad de ejercicios del examen y una leyenda que indique si aprobó o no.

12. Escribir un programa que cuente cúantas veces aparecen cada una de las vocales en una
cadena. No importa si la vocal aparece en mayúscula o en minúscula.
13. Escribir un programa que compare dos strings y devuelva True si el primero es la versión
capitalizada del segundo.
Nota: Por ejemplo, la versión capitalizada de la palabra “programar” es
“PROGRAMAR”.

14. Mastermind: Cada vez que se empieza un partido, el programa debe “eligir” un número de
cuatro cifras (sin cifras repetidas), que será el código que el jugador debe adivinar en la
menor cantidad de intentos posibles. Cada intento consiste en una propuesta de un código
posible que tipea el jugador, y una respuesta del programa. Las respuestas le darán pistas al
jugador para que pueda deducir el código.
Estas pistas indican cuán cerca estuvo el número propuesto de la solución a través de dos
valores: la cantidad de aciertos es la cantidad de dígitos que propuso el jugador que también
están en el código en la misma posición. La cantidad de coincidencias es la cantidad de
digitos que propuso el jugador que también están en el código pero en una posición distinta.
Por ejemplo, si el código que eligió el programa es el 2607, y el jugador propone el 1406, el
programa le debe responder un acierto (el 0, que está en el código original en el mismo
lugar, el tercero), y una coincidencia (el 6, que también está en el código original, pero en la
segunda posición, no en el cuarto como fue propuesto). Si el jugador hubiera propuesto el
3591, habría obtenido como respuesta ningún acierto y ninguna coincidencia, ya que no hay
números en común con el código original, y si se obtienen cuatro aciertos es porque el
jugador adivinó el código y ganó el juego.
El programa, entonces, debe generar un número que el jugador no pueda predecir. A
continuación, debe pedirle al usuario que introduzca un número de cuatro cifras distintas, y
cuando éste lo ingresa, procesar la propuesta y evaluar el número de aciertos y de
coincidencias que tiene de acuerdo al código elegido. Si es el código original, se termina el
programa con un mensaje de felicitación. En caso contrario, se informa al jugador la
cantidad de aciertos y la de coincidencias, y se le pide una nueva propuesta. Este proceso se
repite hasta que el jugador adivine el código.

15. Escribir una función que dada una cadena de caracteres, devuelva:
    1. La primera letra de cada palabra. Por ejemplo, si recibe 'Universal Serial Bus' debe
    devolver 'USB'.
    2. Dicha cadena con la primera letra de cada palabra en mayúsculas. Por ejemplo, si recibe
    'república argentina' debe devolver 'República Argentina'.
    3. Las palabras que comiencen con la letra ‘A’. Por ejemplo, si recibe 'Antes de ayer' debe
    devolver 'Antes ayer'

16. Escribir funciones que dada una cadena de caracteres:
    1. Devuelva solamente las letras consonantes. Por ejemplo, si recibe 'algoritmos' o
    'logaritmos' debe devolver 'lgrtms' .
    2. Devuelva solamente las letras vocales. Por ejemplo, si recibe 'sin consonantes' debe
    devolver 'i ooae'.
    3. Reemplace cada vocal por su siguiente vocal. Por ejemplo, si recibe 'vestuario' debe
    devolver 'vistaerou'.
    4. Indique si se trata de un palíndromo. Por ejemplo, 'anita lava la tina' es un palíndromo
    (se lee igual de izquierda a derecha que de derecha a izquierda).

17. Procesamiento de telegramas. Un oficial de correos decide optimizar el trabajo de su
oficina cortando todas las palabras de más de cinco letras a sólo cinco letras (e indicando
que una palabra fue cortada con el agregado de una arroba). Además elimina todos los
espacios en blanco de más. Por ejemplo, al texto " Llego mañana alrededor del mediodía "
se transcribe como "Llego mañan@ alred@ del medio@". Por otro lado cobra un valor para
las palabras cortas y otro valor para las palabras largas (que deben ser cortadas).
    1. Escribir una función que reciba un texto, la longitud máxima de las palabras, el costo de
    cada palabra corta, el costo de cada palabra larga, y devuelva como resultado el texto del
    telegrama y el costo del mismo.
    2. Los puntos se reemplazan por la palabra especial ”STOP”, y el punto final (que puede
    faltar en el texto original) se indica como ”STOPSTOP”. Al texto: " Llego mañana
    alrededor del mediodía. Voy a almorzar " Se lo transcribe como: "Llego mañan@
    alred@ del medio@ STOP Voy a almor@ STOPSTOP".

18. Inversión de listas
    1. Realizar una función que, dada una lista, devuelva una nueva lista cuyo contenido sea
    igual a la original pero invertida. Así, dada la lista ['Di', 'buen', 'día', 'a', 'papa'], deberá
    devolver ['papa', 'a', 'día', 'buen', 'Di'].
    2. Realizar otra función que invierta la lista, pero en lugar de devolver una nueva,
    modifique la lista dada para invertirla, sin usar listas auxiliares.
