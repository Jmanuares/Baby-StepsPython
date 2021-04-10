
def bisiesto(año):
    if año % 4 == 0 and año % 100 == 0:
        if año % 400 == 0:
            return "Es bisiesto"
        else:
            return "No es bisiesto"
    elif año % 4 == 0:
        return "Es bisiesto"



def mesdia(mes):
    if mes == 1 or mes == 3 or mes == 4 or mes == 6 or mes == 7 or mes == 10 or mes == 12:
        return "Tiene 31 dias"
    if mes == 2:
        return "Tiene 28 dias"
    if mes == 5 or mes == 8 or mes == 9 or mes == 11:
        return "Tiene 30 dias"


funcion= int(input("""Que funcion desea realizar
1.bisiesto
2.dias del mes
"""))
if funcion == 1:
    año = int(input("ingrese el año "))
    print(bisiesto(año))
elif funcion == 2:
    mes = int(input("""Ingrese el mes del cual se quieren saber los dias
    1.enero / 2.febrero / 3.marzo / 4.abril / 5.mayo / 6.junio
    7.julio / 8.agosto / 9.septiembre / 10.octubre / 11.noviembre
    12.diciembre
    """))
    print(mesdia(mes))
