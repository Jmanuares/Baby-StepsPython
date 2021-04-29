"""  Implementar algoritmos (en forma de función) que permitan:

 Calcular el perímetro de un rectángulo dada su base y su altura.
 Calcular el área de un rectángulo dada su base y su altura.
 Calcular el área de un rectángulo (alineado con los ejes x e y ) dadas sus coordenadas x1,x2, y1,y2.
 Calcular el perímetro de un círculo dado su radio.
 Calcular el área de un círculo dado su radio.
 Calcular el volumen de una esfera dado su radio.
 Dados los catetos de un triángulo rectángulo, calcular su hipotenusa. """

def p_rectangulo(base,altura):
    if base < 1 or altura < 1:
        print("no ingrese numeros negativos")
    else:
        perimetro = (base*2 + altura*2)
        return perimetro
    
    
def a_rectangulo(base,altura):
    if base < 1 or altura < 1:
        print("no ingrese numeros negativos")
    else:
        area = (base * altura)
        return area


def a_coordenadas(x1,x2,y1,y2):
    if x1 < 1 or y2 < 1 or y1 < 1 or x2 < 1:
        print("no ingrese numeros negativos")
    else:
        base = (x2-x1)
        altura = (y2-y1)
        area = base*altura
        return area

def p_circulo(radio):
    if radio < 1:
        print("no ingrese numeros negativos")
    else:
        perimetro = (2*radio*3.14)
        return perimetro

def a_circulo (radio):
    if radio < 1:
        print("no ingrese numeros negativos")
    else:
        area = (3.14 * (radio**2))
        return area

def v_esfera (radio):
    if radio < 1:
        print("no ingrese numeros negativos")
    else:
        volumen = 4/3 * 3.14 * radio ** 3
        return volumen

def hipotenusa (cateto1,cateto2):
    if cateto1 < 1 or cateto2 < 1:
        print("no ingrese numeros negativos")
    else:
        hipotenusa = (cateto1**2+cateto2**2)**0.5
        return hipotenusa
    



try:
    funcion = int(input("""¿Que desea hacer? escoja un numero"
    1. perimetro de un rectangulo
    2. area de un rectangulo
    3. area de un rectangulo basado en x e y
    4. perimetro de un circulo
    5. area de un circulo
    6. volumen de una esfera
    7. calcular la hipotenusa
    """))
except:
    print("Respuesta invalida")
    exit()
#pide que funcion se quiere utilizar y valida que sea un numero
if funcion == 1: 
    base = int(input("Ingrese la base del rectangulo "))
    altura = int(input("Ingrese la altura del rectangulo "))
    print(p_rectangulo(base,altura))

elif funcion == 2:

    base = int(input("Ingrese la base del rectangulo "))
    altura = int(input("Ingrese la altura del rectangulo "))
    print(a_rectangulo(base,altura))

elif funcion == 3:

    x1 = int(input("Ingrese la coordenada en x de inicio del rectangulo "))
    x2 = int(input("Ingrese la coordenada en x de fin del rectangulo "))
    y1 = int(input("Ingrese la coordenada en y de inicio del rectangulo "))
    y2 = int(input("Ingrese la coordenada en y de fin del rectangulo "))
    print(a_coordenadas(x1,x2,y1,y2))

elif funcion == 4:

    radio= int(input("Ingrese el radio del circulo "))
    print(p_circulo(radio))

elif funcion == 5:

    radio= int(input("Ingrese el radio del circulo "))
    print(a_circulo(radio))

elif funcion == 6:

    radio= int(input("Ingrese el radio de la esfera "))
    print(a_circulo(radio))

elif funcion == 7:

    cateto1= int(input("ingrese uno de los cateto"))
    cateto2= int(input("ingrese el otro"))
    print(hipotenusa(cateto1,cateto2))

else:
    print("Su respuesta no cumple con los parametros")
    

