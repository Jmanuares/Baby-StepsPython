""" Utilizando la función randrange del módulo random, escribir un programa que tenga un número aleatorio secreto, y luego permita al usuario ingresar números
 y le indique si son menores o mayores que el número a adivinar, hasta que el usuario ingrese el número correcto """
import random
from helper import numero
numRandom = (random.randrange(1, 1000))

while True:
    numAdivinado = input("""Adivina un numero del 1 al 1000
    """)
    if not numero(numAdivinado):
        print("Eso no es un numero!!!")
        continue
    else:
        int(numAdivinado)
        if int(numAdivinado) < numRandom:
            print("El numero es mayor")
        elif int(numAdivinado) > numRandom:
            print("El numero es menor")
        elif int(numAdivinado) == numRandom:
            print("FELICITACIONES ADIVINO EL NUMERO")
            break
