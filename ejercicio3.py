""" Implementar un algoritmo (en una o más funciones) que, dado un número entero numero, permita calcular su factorial."""


def factorial(numero): # calcula el factorial de un numero
    if numero == 0:
        factorial = 0
    else:
        factorial = 1
        for posicion in (range(1, numero)):
            auxiliar = factorial * posicion
            # print(f"auxiliar = posicion({posicion}) * factorial({factorial}) = {auxiliar}")
            # factorial1 = factorial
            factorial = factorial + auxiliar 
            # print(f"factorial = factorial({factorial1}) + auxiliar({auxiliar}) = {factorial}") 
    return factorial
    # en esta funcion lo comentado es para probar el funcionamiento del factorial que al principio no entendi muy bien porque funcionaba


try:
    numero = int(input("ingrese un numero para saber su factorial "))
    print(factorial(numero))
except:
    print("Dato invalido")