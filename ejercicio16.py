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
        "1":"a",
        "2":"e",
        "3":"i",
        "4":"o",
        "5":"u", 
        }

funcion = input("""¿Que desea hacer? escoja un numero"
1. Solo consonantes
2. Solo vocales
3. Siguiente vocal
""")
palabra = input("ingrese una cadena de caracteres unicode: ")
letras = ""


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
        if letra in "AEIOUaeiou ":
            palabra = letras + letra 
    print(letras)

