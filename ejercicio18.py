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

palabrasR=[]
palabras = texto.split()

def invertir(texto):
    palabras = texto.split()
    for i in range(len(palabras)):
        palabrasR.append(palabras[-i-1])
    for i in range(len(palabrasR)):
        print(palabrasR[i])

def invertirLs(texto):
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


