"""Escribir un programa (con al menos una función)
que convierta un valor dado en grados Fahrenheit a grados Celsius. Recordar que la fórmula para la conversión es: F = 9/5 C + 32."""
def Conversion(Faren): 

    Celsius = (faren-32)* 5/9

    return Celsius

faren = int(input("Ingrese grados Farenheit "))
print(Conversion(faren))