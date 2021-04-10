def Conversion(celsius): 
    Faren = (celsius-32)* 5/9
    return Faren

for Celsius in range(0,130,10):
    cambio = (Conversion(celsius)) 
    print(f"{celsius} C° =  {str(cambio)[:5]}")
    
    