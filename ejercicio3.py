def factorial(n):
    r = 1
    for i in (range(1, n)):
        a = r * i
        r = r + a  
    return r
        

n = int(input("ingrese un numero para saber su factorial "))
print(factorial(n))