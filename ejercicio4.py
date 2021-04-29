"""Escribir un programa (con al menos una función)
que convierta un valor dado en grados Fahrenheit a grados Celsius. Recordar que la fórmula para la conversión es: F = 9/5 C + 32."""
def conversion(Faren): 

    Celsius = (faren-32)* 5/9

    return Celsius
try:
    faren = int(input("Ingrese grados Farenheit "))
    print(conversion(faren))
except:
    print("Dato invalido")