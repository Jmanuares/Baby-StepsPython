
def bisiesto(año):
    if año % 4 == 0 and año % 100 == 0:
        if año % 400 == 0:
            return "Es bisiesto"
        else:
            return "No es bisiesto"
    elif año % 4 == 0:
        return "Es bisiesto"



def mesdia(mes):
    from datetime import date
    from calendar import monthrange
    
    cantidad_de_dias= monthrange(2011, mes)[1]
    return cantidad_de_dias



if funcion == 1:

    año = int(input("ingrese el año "))
    print(bisiesto(año))

elif funcion == 2:
    mes = int(input("""Ingrese el mes del cual se quieren saber los dias
    1.enero / 2.febrero / 3.marzo / 4.abril / 5.mayo / 6.junio
    7.julio / 8.agosto / 9.septiembre / 10.octubre / 11.noviembre
    12.diciembre
    """))
    print(f"Tiene {mesdia(mes)} Dias")
    
    
    funcion= int(input("""Que funcion desea realizar
1.bisiesto
2.dias del mes
"""))
