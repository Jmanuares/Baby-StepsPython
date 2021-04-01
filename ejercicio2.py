def p_rectangulo(B,H):
    if B < 1 or H < 1:
        print("no ingrese numeros negativos")
    else:
        perimetro = (B + H)*2
        return perimetro
    
    
def a_rectangulo(B,H):
    if B < 1 or H < 1:
        print("no ingrese numeros negativos")
    else:
        area = (B * H)
        return area


def a_coordenadas(x1,x2,y1,y2):
    if x1 < 1 or y2 < 1 or y1 < 1 or x2 < 1:
        print("no ingrese numeros negativos")
    else:
        area = (x2-x1)*(y2-y1)
        return area

def p_circulo(r):
    if r < 1:
        print("no ingrese numeros negativos")
    else:
        perimetro = (2*r*3.14)
        return perimetro

def a_circulo (r):
    if r < 1:
        print("no ingrese numeros negativos")
    else:
        area = (3.14 * (r**2))
        return area

def V_esfera (r):
    if r < 1:
        print("no ingrese numeros negativos")
    else:
        volumen = 4/3 * 3.14 * r ** 3
        return volumen

def hipotenusa (c1,c2):
    if c1 < 1 or c2 < 1:
        print("no ingrese numeros negativos")
    else:
        hipotenusa = (c1+c2)**2
        return hipotenusa
    




funcion = int(input("""¿Que desea hacer? escoja un numero"
1. perimetro de un rectangulo
2. area de un rectangulo
3. area de un rectangulo basado en x e y
4. perimetro de un circulo
5. area de un circulo
6. volumen de una esfera
7. calcular la hipotenusa
"""))
if funcion == 1: 
    B = int(input("Ingrese la base del rectangulo "))
    H = int(input("Ingrese la altura del rectangulo "))
    print(p_rectangulo(B,H))

elif funcion == 2:

    B = int(input("Ingrese la base del rectangulo "))
    H = int(input("Ingrese la altura del rectangulo "))
    print(a_rectangulo(B,H))

elif funcion == 3:

    x1 = int(input("Ingrese la coordenada en x de inicio del rectangulo "))
    x2 = int(input("Ingrese la coordenada en x de fin del rectangulo "))
    y1 = int(input("Ingrese la coordenada en y de inicio del rectangulo "))
    y2 = int(input("Ingrese la coordenada en y de fin del rectangulo "))
    print(a_coordenadas(x1,x2,y1,y2))

elif funcion == 4:

    r= int(input("Ingrese el radio del circulo "))
    print(p_circulo(r))

elif funcion == 5:

    r= int(input("Ingrese el radio del circulo "))
    print(a_circulo(r))

elif funcion == 6:

    r= int(input("Ingrese el radio de la esfera "))
    print(a_circulo(r))

elif funcion == 7:

    c1= int(input("ingrese uno de los cateto"))
    c2= int(input("ingrese el otro"))
    print(hipotenusa(c1,c2))

else:
    print("Su respuesta no cumplo parametros")
    

