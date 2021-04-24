"""  Escribir una función que dada una cadena de caracteres, devuelva:
    1. La primera letra de cada palabra. Por ejemplo, si recibe 'Universal Serial Bus' debe
    devolver 'USB'.
    2. Dicha cadena con la primera letra de cada palabra en mayúsculas. Por ejemplo, si recibe
    'república argentina' debe devolver 'República Argentina'.
    3. Las palabras que comiencen con la letra ‘A’. Por ejemplo, si recibe 'Antes de ayer' debe
    devolver 'Antes ayer' """

funcion = input("""¿Que desea hacer? escoja un numero"
1. Separar las primaras siglas
2. Capitalizar las primeras letra
3. Filtrar palabras
""")
siglas = ""
frase = ""

if funcion == "1":
    texto = input("Ingrese una cadena de caracteres Unicode: ")
    cadena = (texto.split(" "))
    for palabra in cadena:
        siglas = siglas + palabra[0]
    print(siglas.upper())

elif funcion == "2":
    texto = input("Ingrese una cadena de caracteres Unicode: ")
    cadena = (texto.split(" "))
    for palabra in cadena:
        frase = frase + palabra.capitalize()  + " "
    print(frase)

elif funcion == "3":
    texto = input("Ingrese una cadena de caracteres Unicode: ")
    Letra = input("Ingrese la letra por la que quiere separar las palabras:")
    cadena = (texto.split(" "))
    for palabra in cadena:
        if palabra[0] == Letra or palabra[0] == Letra.upper() :
            frase = frase + palabra  + " "
    print(frase)

else: 
    print("Respuesta invalida")
