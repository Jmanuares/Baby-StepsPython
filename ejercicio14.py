"""Genera un numero de 4 cifras distintas y permite que el usuario vaya ingresando
numeros hasta que coincidan."""
import random


numRandom = str(random.randrange(1000, 9999))
""" genera un numero random de 4 cifras """
resultado = ""
aciertos = 0


for numero in numRandom: 
    while numero in resultado:
        numero = str(random.randrange(0, 9))
    resultado = resultado + numero
""" hace que el numero random no repita cifras """

while True: 
    """ dice cuantas coincidencias o aciertos entre el numero random y el codigo adivinado """

    coincidencia = 0
    aciertos = 0
    try:
        adivinar= int(input("Adivine el codigo(los cuatro digitos deben ser diferentes): "))

        if adivinar > 1000: # me fijo si estan los mismos numeros eso es una coincidencia
            adivinar = str(adivinar)
            for numero in numRandom:
                if numero in str(adivinar):
                    coincidencia = coincidencia + 1

            for i in range(1,5): # me fijo si estan los mismos numeros en la misma posicion eso es un acierto
                    if(adivinar[i-1:i] == resultado[i-1:i]):
                        aciertos +=1
                        # si hay un acierto mas tiene que haber una coincidencia menos 
            
            
            if int(adivinar) != int(resultado):
                print(f"tuviste {coincidencia} coincidencias y {aciertos} aciertos")
                continue

            elif  int(adivinar) == int(resultado):
                print("Felicidades ganaste")
            break

        else:
            print("No empieza por 0 y debe tener 4 digitos")

    except:
        print("Codigo invalido")
