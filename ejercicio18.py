""" 18. Inversión de listas
    1. Realizar una función que, dada una lista, devuelva una nueva lista cuyo contenido sea
    igual a la original pero invertida. Así, dada la lista ['Di', 'buen', 'día', 'a', 'papa'], deberá
    devolver ['papa', 'a', 'día', 'buen', 'Di'].
    2. Realizar otra función que invierta la lista, pero en lugar de devolver una nueva,
    modifique la lista dada para invertirla, sin usar listas auxiliares. """

    
try:
    funcion = int(input("""¿Que desea hacer? (son iguales)
    1. invertir texto con lista auxiliar
    2. invertir texto sin lista auxiliar 
    """))
    texto = input("ingrese una cadena de caracteres unicode: ")
except:
    print("Ingreso de datos erroneos")


listapalabrasalrevez=[]
palabras = texto.split()

def invertir(texto):
    """ Recibe:
        texto:<string>
    Invierte el texto con una lista auxiliar """
    palabras = texto.split()
    for i in range(len(palabras)): # añade las palabras de la lista "palabras" a una lista vacia "listapalabrasalrevez" pero de atras para adelante
        listapalabrasalrevez.append(palabras[-i-1])
    for i in range(len(listapalabrasalrevez)): # muestra listapalabrasalrevez
        print(listapalabrasalrevez[i])


def invertirLs(texto):
    """Recibe:
        texto:<string>
    Invierte el texto sin una lista auxiliar """
    for i in range(len(palabras)):
        palabras.append(palabras[len(palabras)-i-1])
        palabras.remove(palabras[len(palabras)-i-1])
        # pone la primer palabra al final y la elimina del principio
    for i in range(len(palabras)):
        print(palabras[i])


#interfaz de elegir funcion
if funcion == "1": 
    invertir(texto)
elif funcion == "2":
    invertirLs(texto)
else:
    print("Respuesta invalida")


