""" 16. Escribir funciones que dada una cadena de caracteres:
    1. Devuelva solamente las frase frase. Por ejemplo, si recibe 'algoritmos' o
    'logaritmos' debe devolver 'lgrtms' .
    2. Devuelva solamente las frase vocales. Por ejemplo, si recibe 'sin frase' debe
    devolver 'i ooae'.
    3. Reemplace cada vocal por su siguiente vocal. Por ejemplo, si recibe 'vestuario' debe
    devolver 'vistaerou'.
    4. Indique si se trata de un palíndromo. Por ejemplo, 'anita lava la tina' es un palíndromo
    (se lee igual de izquierda a derecha que de derecha a izquierda). """
vocales=  {
        "a":"e",
        "e":"i",
        "i":"o",
        "o":"u",
        "u":"a",
        "A":"E",
        "E":"I",
        "I":"O",
        "O":"U",
        "U":"A",    
        }


def soloconsonantes(): #saca las vocales del texto dado
    frase = ""
    for letra in palabra:
                if not letra in "AEIOUaeiou":
                    frase = frase + letra 
    return frase


def solovocales(): #saca las consonantes del texto dado
    frase = ""
    for letra in palabra:
            if letra in "AEIOUaeiou ":
                frase = frase + letra 
    return frase

def siguientevocal(): #cambia las vocales del texto dado a la siguiente por ejemplo si es a va a ser e
    frase = ""
    for letra in palabra:
            if letra in "AEIOUaeiou":
                letra = vocales[str(letra)]
            frase = frase + letra 
    return frase

def palindromo(palabra): #indica si el texto es un palindromo
    frase = palabra.replace(" ","")
    """ esta funcion es la funcion replace por si no se podia utilizar
    frase = "" 
    for letra in palabra:
        if not letra in " ":
            frase = frase + letra  """
    if frase == frase[::-1]:
        return 1
    else:
        return 0


try:
    funcion = int(input("""¿Que desea hacer? escoja un numero"
    1. Solo solo consonantes
    2. Solo vocales
    3. Siguiente vocal
    4. Palindromo
    """))
except:
    print("Dato invalido")
    exit()


if funcion == 1 or funcion == 2 or funcion == 3 or funcion == 4:
    palabra = input("ingrese una cadena de caracteres unicode: ")
    frase = ""
    letra = ""
    if funcion == 1: 
        print(soloconsonantes())

    elif funcion == 2:
        print(solovocales())

    elif funcion == 3:
        print(siguientevocal())

    elif funcion == 4:
        if (palindromo(palabra)) == 1:
            print(f"({palabra}) es un palindromo")
        elif (palindromo(palabra)) == 0:
            print(f"({palabra}) no es un palindromo")
    elif palabra == "":
        print("ingreso de datos erroneo")
else:
    print("ingreso de datos erroneo")
