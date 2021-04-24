""" Escribir un programa que cuente cúantas veces aparecen cada una de las vocales en una cadena.
No importa si la vocal aparece en mayúscula o en minúscula. """

palabra = input("ingrese una cadena de caracteres unicode: ")
cont = 0
for letra in palabra.upper():
    if letra in "AEIOU":
        cont += 1

print(f"LA CADENA DE CARACTERES UNICODE( {palabra.upper()}), TIENE {cont} VOCALES ")