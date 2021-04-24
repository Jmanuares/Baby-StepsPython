""" Implementar un algoritmo (en una o más funciones) que, dado un número entero n, permita calcular su factorial."""
def factorial(n):
    if n == 0:
        r = 0
    else:
        r = 1
        for i in (range(1, n)):
            a = r * i
            r = r + a  
    return r
        

n = int(input("ingrese un numero para saber su factorial "))
print(factorial(n))