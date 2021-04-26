""" Escribir un programa que contenga una contraseña inventada, que le pregunte al usuario la contraseña, y no le permita continuar hasta que la haya ingresado correctamente.

Modificar el programa anterior para que solamente permita una cantidad fija de intentos.
Modificar el programa anterior para que después de cada intento agregue una pausa cada vez mayor, utilizando la función sleep del módulo time.
Modificar el programa anterior para que sea una función que devuelva si el usuario ingresó o no la contraseña correctamente, mediante un valor booleano (True o False). """

from time import sleep

espera = 0
intentos = 0
def valid(password):
    if password == "contraseña123":    
        return 1
    else:
        return 0

while intentos != 5:
    password = str(input("Ingresar contraseña "))
    if valid(password) != 1:
        print("""CONTRASEÑA INCORRECTA
        Por favor espere""")
        espera = espera + 2
        intentos = intentos + 1
        cont = espera
        for i in range(1,espera + 1):
            cont = cont - 1
            sleep(1)
            print(cont + 1)
    else:
        print("CONTRASEÑA CORRECTA")
        break
if intentos == 5:
    print("CANTIDAD DE INTENTOS MAXIMA ALCANZADA")