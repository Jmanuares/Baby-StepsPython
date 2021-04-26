""" 16. Escribir funciones que dada una cadena de caracteres:
    1. Devuelva solamente las letras letras. Por ejemplo, si recibe 'algoritmos' o
    'logaritmos' debe devolver 'lgrtms' .
    2. Devuelva solamente las letras vocales. Por ejemplo, si recibe 'sin letras' debe
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
letras = ""
frase = ""
letra = ""

def palindromo(palabra):
    frase = palabra.replace(" ","")
    # frase = ""
    # for letra in palabra:
    #     if not letra in " ":
    #         frase = frase + letra 
    if frase == frase[::-1]:
        return 1
    else:
        return 0



funcion = input("""¿Que desea hacer? escoja un numero"
1. Solo consonantes
2. Solo vocales
3. Siguiente vocal
4. Palindromo
""")
if funcion == "1" or funcion == "2" or funcion == "3" or funcion == "4":
    palabra = input("ingrese una cadena de caracteres unicode: ")
    if palabra != "":
        if funcion == "1": 
            for letra in palabra:
                if not letra in "AEIOUaeiou":
                    letras = letras + letra 
            print(letras)

        if funcion == "2":
            for letra in palabra:
                if letra in "AEIOUaeiou ":
                    letras = letras + letra 
            print(letras)

        if funcion == "3":
            for letra in palabra:
                if letra in "AEIOUaeiou":
                    letra = vocales[str(letra)]
                frase = frase + letra 
            print(frase)

        if funcion == "4":
            if (palindromo(palabra)) == 1:
                print(f"({palabra}) es un palindromo")
            elif (palindromo(palabra)) == 0:
                print(f"({palabra}) no es un palindromo")
        else:
            print("Respuesta invalida")
    else:
            print("Respuesta invalida")
else:
    print("Respuesta invalida")
