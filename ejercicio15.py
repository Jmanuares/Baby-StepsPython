"""  Escribir una función que dada una cadena de caracteres, devuelva:
    1. La primera letra de cada palabra. Por ejemplo, si recibe 'Universal Serial Bus' debe
    devolver 'USB'.
    2. Dicha cadena con la primera letra de cada palabra en mayúsculas. Por ejemplo, si recibe
    'república argentina' debe devolver 'República Argentina'.
    3. Las palabras que comiencen con la letra ‘A’. Por ejemplo, si recibe 'Antes de ayer' debe
    devolver 'Antes ayer' """


try:
    funcion = int(input("""¿Que desea hacer? escoja un numero"
    1. Separar las primeras siglas
    2. Capitalizar las primeras letra
    3. Filtrar palabras
    """))
except:
    print("Dato invalido")
    exit()


letras = ""
frase = ""


if funcion == 1:
    """ Separa las primeras siglas y las muestra en mayusculas """
    texto = input("Ingrese una cadena de caracteres Unicode: ")
    cadena = (texto.split(" "))
    # Separa el texto en palabras en la lista "cadena"
    try:
        for palabra in cadena:
            letras = letras + palabra[0]
        # hace que el string letras solo se quede con la primera letra de la palabra es decir la posicion [0]
        print(letras.upper())
    except:
        print("ingreso de datos erroneo")


elif funcion == 2:
    """ Capitaliza las primer letra de cada palabra """
    texto = input("Ingrese una cadena de caracteres Unicode: ")
    cadena = (texto.split(" "))
    # Separa el texto en palabras en la lista "cadena"
    try:
        for palabra in cadena:
            frase = frase + palabra.capitalize()  + " "
        # .capitalize devuelve la misma palabra pero con la primera letra mayuscula
        print(frase)
    except:
        print("ingreso de datos erroneo")


elif funcion == 3: 
    """ Filtra palabras que empiecen por la letra que da el usuario """
    texto = input("Ingrese una cadena de caracteres Unicode: ")
    Letra = input("Ingrese la letra por la que quiere separar las palabras:")
    cadena = (texto.split(" "))
    # Separa el texto en palabras en la lista "cadena"
    try:
        for palabra in cadena:
            if palabra[0] == Letra or palabra[0] == Letra.upper() :
                frase = frase + palabra + " "
        print(frase)
    except:
        print("ingreso de datos erroneo")
else: 
    print("Respuesta invalida")
