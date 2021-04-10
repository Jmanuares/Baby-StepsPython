def Conversion(Faren): 

    Celsius = (faren-32)* 5/9

    return Celsius

faren = int(input("Ingrese grados Farenheit "))
print(Conversion(faren))