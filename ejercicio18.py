""" 18. Inversión de listas
    1. Realizar una función que, dada una lista, devuelva una nueva lista cuyo contenido sea
    igual a la original pero invertida. Así, dada la lista ['Di', 'buen', 'día', 'a', 'papa'], deberá
    devolver ['papa', 'a', 'día', 'buen', 'Di'].
    2. Realizar otra función que invierta la lista, pero en lugar de devolver una nueva,
    modifique la lista dada para invertirla, sin usar listas auxiliares. """

funcion = input("""¿Que desea hacer? (son iguales)
1. invertir texto con lista auxiliar
2. invertir texto sin lista auxiliar 
""")
texto = input("ingrese una cadena de caracteres unicode: ")

listapalabrasalrevez=[]
palabras = texto.split()

def invertir(texto): #Invierte el texto con una lista auxiliar
    palabras = texto.split()
    for i in range(len(palabras)):
        listapalabrasalrevez.append(palabras[-i-1])
    for i in range(len(listapalabrasalrevez)):
        print(listapalabrasalrevez[i])

def invertirLs(texto): #Invierte el texto sin una lista auxiliar
    for i in range(len(palabras)):
        palabras.append(palabras[len(palabras)-i-1])
        palabras.remove(palabras[len(palabras)-i-1])
    for i in range(len(palabras)):
        print(palabras[i])


if funcion == "1": 
    invertir(texto)
elif funcion == "2":
    invertirLs(texto)
else:
    print("Respuesta invalida")


