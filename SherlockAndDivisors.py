#!/bin/python3
#Importamos librerias
import math
import os
import random
import re
import sys
#Definimos la funcion
def divisors(n):
    count = 0  # Variable para contar los divisores pares
    for i in range(1, int(math.sqrt(n)) + 1):  # Iteramos desde 1 hasta la raíz cuadrada de n
        if n % i == 0:  # Verificamos si i es un divisor de n
            if i % 2 == 0:  # Si i es par, incrementamos el contador
                count += 1
            if i != n // i and (n // i) % 2 == 0:  # Verificamos si el divisor complementario es par
                count += 1
    return count #Retornamos la variable count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())  # Lee el número de casos de prueba

    for t_itr in range(t):  # Iteramos sobre los casos de prueba
        n = int(input().strip())  # Lee el valor de entrada para el caso de prueba actual

        result = divisors(n)  # Calcula el número de divisores pares

        fptr.write(str(result) + '\n')  # Escribe el resultado en el archivo de salida

    fptr.close()  # Cierra el archivo de salida
