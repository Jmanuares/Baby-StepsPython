def compararMayor(n1,n2):
    if n1 > n2:
        return n1
    else:
        return n2

num1=float(input("ingrese el primer numero: "))
num2=float(input("ingrese el segundo numero: "))
num3=float(input("ingrese el tercer numero: "))
num4=float(input("ingrese el cuarto numero: "))


mul1= num1 * num2 
mul2= num1 * num3
mul3= num1 * num4   
mul4= num2 * num3
mul5= num2 * num4
mul6= num3 * num4

mayor1= compararMayor(mul1,mul2)    
mayor2= compararMayor(mayor1,mul3) 
mayor3= compararMayor(mayor2,mul4) 
mayor4= compararMayor(mayor3,mul5)
Mayor= compararMayor(mayor4,mul6) 
print("El mayor producto es", Mayor)
