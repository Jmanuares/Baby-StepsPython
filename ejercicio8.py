
""" Escribir un programa que reciba como entrada un entero representando un año (por ejemplo 751, 1999, o 2158), y muestre por pantalla el mismo año escrito en números romanos."""
Info = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"), (90, "XC"),
(50, "L"), (40, "XL"), (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")]


def convertirRom(numero): 
    """ Recibe:
            numero:<int>
    Convierte el numero dado al mismo numero en romanos """
    romanos = ""
    while numero > 0:
        for lsNume, lsLetra in Info:
            while numero >= lsNume:
                romanos = romanos + lsLetra
                numero = numero - lsNume
    # utiliza la lista info y a medida que le va restando el numero de la lista que puede ira sumando a un string las letras
    return romanos


try:
    numero = int(input("Ingrese un numero: "))
    if numero == 0:
        print("No se puede representar el 0 en numeros romanos")
    elif numero < 0:
        print("No se pueden ingresar numero negativos")
    else:
        print(f"{numero} escrito en numero romanos es {convertirRom(numero)}")
except:
    print("Ingreso un dato no valido")