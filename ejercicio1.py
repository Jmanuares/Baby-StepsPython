""" Escribir un programa que pregunte al usuario:

Su nombre, y luego lo salude.
Dos números, y luego muestre el producto. """

from helper import numero


while True:
    valido = 1
    nombre = input("Introduzca su nombre ")
    for letra in nombre:
        if letra in "123456789":
            valido = 0
    if valido == 0:
        print("No ingrese numeros")
        continue  
    # valida que no haya un numero en el nombre
    elif nombre == "":
        print ("No escribio nada")
    # Valida que el usuario haya escrito algo
     
    else: 
        print(f"hola {nombre}")
        break

    
try:
    num1 = int(input("Introduzca el primer numero para ser multiplicado "))
    num2 = int(input("Introduzca el segundo numero para ser multiplicado "))
    producto = num1 * num2
    print (f"el producto de ({num1}) y ({num2}) es {producto}")
except: 
    print("Dato invalido")
