""" Utilizando la función randrange del módulo random, escribir un programa que tenga un número aleatorio secreto, y luego permita al usuario ingresar números
 y le indique si son menores o mayores que el número a adivinar, hasta que el usuario ingrese el número correcto """
import random
from helper import numero
num = (random.randrange(1, 1000))

while True:
    adiv = input("""Ingrese un numero del 1 al 1000
    """)
    if not numero(adiv):
        print("Favor de ingresar un numero".upper())
        continue
    else:
        int(adiv)
        if int(adiv) < num:
            print("El numero es mayor")
        elif int(adiv) > num:
            print("El numero es menor")
        elif int(adiv) == num:
            print("FELICITACIONES ADIVINO EL NUMERO")
            break
