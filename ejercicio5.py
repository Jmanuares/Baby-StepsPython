def Conversion(Faren): 

    Celsius = (faren-32)* 5/9

    return Celsius

for faren in range(0,130,10):
    cambio = (Conversion(faren)) 
    print(repr(faren) + "C° = " + (str(cambio)[:5]))
    
    