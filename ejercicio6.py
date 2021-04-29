""" Escribir una función que, dados cuatro números, devuelva el mayor producto de dos de ellos.
Por ejemplo, si recibe los números 1, 5, -2, -4 debe devolver 8, que es el producto más grande que se puede obtener entre ellos (8 = −2 × −4). """
def compararmayor(n1,n2):
    if n1 > n2:
        return n1
    else:
        return n2
try:
    num1=float(input("ingrese el primer numero: "))
    num2=float(input("ingrese el segundo numero: "))
    num3=float(input("ingrese el tercer numero: "))
    num4=float(input("ingrese el cuarto numero: "))
except:
    print("Ingrese numero por favor")
    exit()


mul1= num1 * num2 
mul2= num1 * num3
mul3= num1 * num4   
mul4= num2 * num3
mul5= num2 * num4
mul6= num3 * num4

mayor1= compararmayor(mul1,mul2)    
mayor2= compararmayor(mayor1,mul3) 
mayor3= compararmayor(mayor2,mul4) 
mayor4= compararmayor(mayor3,mul5)
Mayor= compararmayor(mayor4,mul6) 
print("El mayor producto es", Mayor)
