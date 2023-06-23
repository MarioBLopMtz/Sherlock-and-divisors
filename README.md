# Sherlock-and-divisors

Descripción del problema: En este problema una persona llamada Sherlock un numero N y le pregunta cual es el numero de divisores de N que son divisibles por 2

Solución del problema: Para este problema, lo ideal fue inicializar una variable llamada count a 0 para utilizarla como contador, para despues iniciar un ciclo for, donde vamos estar iterando el rango de numeros desde 1 hasta la raiz cuadrada de N, esto porque asi garantizamos todos los numeros que son divisibles entre N, verificamos si esos numeros si son divisibles entre N sacando su modulo y si es igual a 0 quiere decir que si lo es, luego verificamos si  ese divisor es divisible entre dos igual con su modulo e incrementamos el contador sumandole 1 si es verdad, volvemos a verificamos que la division entera entre N y la variable que utilizamos para iterar es diferente de i, esto para no contar el mismo divisor dos veces y si el cociente de N entre i es divisible entre dos, igual incrementamos el contador sumandole 1 si es verdad, cuando termine de iterar el ciclo for, retornara el valor que tiene la variable count y ese es el numero de divisores de N que son divisibles por 2.

Intrucciones de ejecución de solución:

  1. Abrir el link (https://www.hackerrank.com/challenges/sherlock-and-divisors/problem?isFullScreen=true).
  2. Abrir el archivo SherlockAndDivisors.py y copiarlo.
  3. Sustituir el contenido de la consola que hay en la página con el que copiamos del archivo.
  4. Correr el código.

Ejemplos de valores de entrada y salidas esperadas: Entrada: 2, 9 8 Salida: 0, 3, 3
