""" Utilice el programa anterior para generar (imprimir en pantalla) una tabla de conversión de temperaturas,
desde 0 °F hasta 120 °F, de 10 en 10. Nota: La forma ideal es haber implementado en el ejercicio anterior una función para hacer la traducción entre Fahrenheit y Celcius. En este ejercicio, lo que resta es crear, para este ejercicio, una función que llame a la anterior varias veces. """


def conversion(celsius): 
    """ convierte grados celsius a farenheit """
    faren = (celsius-32)* 5/9
    return faren

for celsius in range(0,130,10): # printea la tabla de grados
    cambio = (conversion(celsius)) 
    print(f"{celsius} C° =  {str(cambio)[:5]} F")

