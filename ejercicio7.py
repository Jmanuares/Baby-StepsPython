
dias = {
        "1":31,
        "2":28,
        "3":31,
        "4":30,
        "5":31,
        "6":30,
        "7":31,
        "8":31,
        "9":30,
        "10":31,
        "11":30,
        "12":31
    }


def bisiesto(año):
    if año % 4 == 0 and año % 100 == 0:
        if año % 400 == 0:
            return "Es bisiesto"
        else:
            return "No es bisiesto"
    elif año % 4 == 0:
        return "Es bisiesto"

def mesdia(mes):
    if bisiesto(año) == "Es bisiesto":
        dias["2"] = 29
    return dias[str(mes)]


def valid(dia,mes,año):
    if dia > 0:
        if 0 < mes and mes < 13:
            if dia > mesdia(mes):
                return "Fecha no valida"
            else:
                return "Es valido"
        else:
            return "Fecha no valida"
    else:
        return "Fecha no valida"

def faltan(dia,mes,año):
    if valid(dia,mes,año) == "Fecha no valida":
        return valid(dia,mes,año)
    elif valid(dia,mes,año) == "Es valido":
        fal= mesdia(mes) - (dia)
        return fal


def findeaño(dia,mes,año):
    if valid(dia,mes,año) == "Es valido":
        mesRestan = 12 - mes
        r=0
        if mesRestan != 0:
            for i in (range(mes, 12)):
                a = mesdia(i)  
                r = r + a  
        fal = r + faltan(dia,mes,año)
        return fal
    else:
        return "Fecha no valida"




func= int(input("""Que funcion desea realizar
1.Bisiesto
2.Dias del mes
3.Fecha valida
4.Cuantos dias faltan para que termine el mes
5.Cuantos dias faltan para que termine el año
"""))

if func == 1:
    año = int(input("ingrese el año "))
    print(bisiesto(año))

elif func == 2:
    mes = int(input("""Ingrese el mes del cual se quieren saber los dias
    1.enero / 2.febrero / 3.marzo / 4.abril / 5.mayo / 6.junio
    7.julio / 8.agosto / 9.septiembre / 10.octubre / 11.noviembre
    12.diciembre
    """))
    año= int(input("Ingrese el año "))
    print(f"Tiene {mesdia(mes)} Dias")

elif func == 3: 
    dia= int(input("Ingrese el dia "))
    mes= int(input("Ingrese el mes "))
    año= int(input("Ingrese el año "))
    print(valid(dia,mes,año))

elif func == 4: 
    dia= int(input("Ingrese el dia "))
    mes= int(input("Ingrese el mes "))
    año= int(input("Ingrese el año "))
    print(faltan(dia,mes,año))
elif func == 5: 
    dia= int(input("Ingrese el dia "))
    mes= int(input("Ingrese el mes "))
    año= int(input("Ingrese el año "))
    print(findeaño(dia,mes,año))