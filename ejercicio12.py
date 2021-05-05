""" Escribir un programa que cuente cúantas veces aparecen cada una de las vocales en una cadena.
No importa si la vocal aparece en mayúscula o en minúscula. """


palabra = input("ingrese una cadena de caracteres unicode: ")
cont = 0


if palabra == "": # revisa cuantas vocales aparecen en la palabra
    print("eso no es una cadena de caracteres unicode")
else:
    for letra in palabra.upper():
        if letra in "AEIOU":
            cont += 1
    print(f"LA CADENA DE CARACTERES UNICODE, {palabra.upper()}, TIENE {cont} VOCALES ")
