
""" 7.Escribir funciones que resuelvan los siguientes problemas:

1. Dado un anio indicar si es bisiesto. (Nota: un anio es bisiesto si es un número divisible por 4, pero no si es divisible por 100, excepto que también sea divisible por 400).
2. Dado un mes, devolver la cantidad de días correspondientes.
3. Dada una fecha (día, mes, anio), indicar si es válida o no.
4. Dada una fecha, indicar los días que faltan hasta fin de mes.
5. Dada una fecha, indicar los días que faltan hasta fin de anio.
6. Dada una fecha, indicar la cantidad de días transcurridos en ese anio hasta esa fecha.
7. Dadas dos fechas (día1, mes1, año1, día2, mes2, anio2), indicar el tiempo transcurrido entre ambas, en anios, meses y días. Nota: en todos los casos, invocar las funciones escritas previamente cuando sea posible. """
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
# diccionario que dice cuantos dias tiene cada mes

try:
    func= int(input("""Que funcion desea realizar
    1.Bisiesto
    2.Dias del mes
    3.Fecha valida
    4.Cuantos dias faltan para que termine el mes
    5.Cuantos dias faltan para que termine el anio
    6.Cuantos dias transcurrieron
    7.diferencia entre fechas
    """))
except:
    print("Respuesta invalida")
    exit()
# eleccion de la funcion y un tryexcept para que el usuario no use strings ni campo vacio

def bisiesto(anio):
    if anio % 4 == 0 and anio % 100 == 0:
        if anio % 400 == 0:
            return 1
        else:
            return 0
    else:
        if anio % 4 == 0:
            return 1
        else:
            return 0
# si el anio es bisiesto 1 es que es y 0 es que no

def mesdia(mes):
    if bisiesto(anio) == 1:
        dias["2"] = 29
        #si el año es bisiesto febrero ( que es 2 ) va a tener 29 dias
    return dias[str(mes)]
    # llama al diccionario dias definido previamente
# cuantos dias hay en el mes

def valid(dia,mes,anio):
    if dia == "" or mes == "" or anio == "":
        return 0
    elif dia > 0:
        if 0 < mes and mes < 13:
            if dia > mesdia(mes):
                return 0
            else:
                return 1
        else:
            return 0
    else:
        return 0
# validar fecha

def faltan(dia,mes,anio):
    if valid(dia,mes,anio) == 0:
        return "Fecha no valida"
    elif valid(dia,mes,anio) == 1:
        faltandias = mesdia(mes) - (dia)
        return faltandias
    #primero valida que la fecha sea valida y despues resta el dia que es "dia" a la cantidad de dias que tiene el mes "mesdia(mes)"
# dias para que termine el mes

def findeaño(dia,mes,anio):
    if valid(dia,mes,anio) == 1:
        mesRestan = 12 - mes
        Diasrestantes=0
        if mesRestan != 0:
            for i in (range(mes, 12)):     
                auxiliar = mesdia(i+1)  
                Diasrestantes = Diasrestantes + auxiliar  
        faltandias = Diasrestantes + faltan(dia,mes,anio)
        return faltandias
    else:
        return "Fecha no valida"
# dias para que termine el anio

def diastranscurridos(dia,mes,anio):
    if valid(dia,mes,anio) == 1:
        diastrans=0
        if bisiesto(anio) == 1:
            diastrans = 366 - findeaño(dia,mes,anio)
        elif bisiesto(anio) == 0:
            diastrans = 365 - findeaño(dia,mes,anio)
        return diastrans
    else:
        return "Fecha no valida"
# dias trancurridos del anio

def difFechas(dia,mes,anio,dia2,mes2,anio2):
    if valid(dia,mes,anio) == 1 or valid(dia2,mes2,anio2) == 1:
        resta = diastranscurridos(dia2,mes2,anio2) + findeaño(dia,mes,anio)
        anios = anio2 - anio
        anio = 0
        meses = 0
        dias = 0
        for i in range(1,anios):
            resta = resta + 365
        while resta != 0:
            if resta - 365 >= 0:
                resta = resta - 365
                anio = anio + 1
            elif resta - 30 >= 0:
                resta = resta - 30
                meses = meses + 1
            elif resta - 1 >= 0:
                resta = resta - 1
                dias = dias + 1
        return (f"entre la fecha {dia}/{mes}/{anio} y {dia2}/{mes2}/{anio2} hay {dias} dias, {meses} meses y {anio} anios")
    else:
        return "Fecha invalida"
# diferencia entre dos fechas dadas por el usuario

# En todas las funciones hay un try, except que no permite al usuario completar campos con strings o dejar campo vacio
if func == 1:
    try:
        anio = int(input("ingrese el anio "))

        if bisiesto(anio) == 1:
            print(f"el anio {anio} es bisiesto")

        elif bisiesto(anio) == 0:
            print(f"el anio {anio} no es bisiesto")
    except:
        print("Respuesta invalida")

elif func == 2:
    try:
        mes = int(input("""Ingrese el mes del cual se quieren saber los dias
        1.enero / 2.febrero / 3.marzo / 4.abril / 5.mayo / 6.junio
        7.julio / 8.agosto / 9.septiembre / 10.octubre / 11.noviembre
        12.diciembre
        """))

        anio= int(input("Ingrese el anio "))

        if valid(1,int(mes),1) == 1:
            print(f"Tiene {mesdia(int(mes))} Dias")
        else:
            print("Mes no valido")

    except:
        print("Respuesta invalida")


elif func == 3: 
    try:
        dia= (int(input("Ingrese el dia ")))
        mes= (int(input("Ingrese el mes ")))
        anio= (int(input("Ingrese el anio ")))
        if valid(dia,mes,anio) == 1:
            print(f"la fecha {dia}/{mes}/{anio} es valida")
        else:
            print(f"la fecha {dia}/{mes}/{anio} es invalida")
    except:
        print("Fecha invalida")


elif func == 4:
    try: 
        dia= (int(input("Ingrese el dia ")))
        mes= (int(input("Ingrese el mes ")))
        anio= (int(input("Ingrese el anio ")))
        print(faltan(dia,mes,anio))
    except:
        print("Respuesta invalida")


elif func == 5: 
    try:
        dia= int(input("Ingrese el dia "))
        mes= int(input("Ingrese el mes "))
        anio= int(input("Ingrese el anio "))
        print(findeaño(dia,mes,anio))
    except:
        print("Respuesta invalida")


elif func == 6: 
    try:
        dia= int(input("Ingrese el dia "))
        mes= int(input("Ingrese el mes "))
        anio= int(input("Ingrese el anio "))
        print(diastranscurridos(dia,mes,anio))
    except:
        print("Respuesta invalida") 


elif func == 7:
    try:
        print("Ingrese la primera fecha")
        dia= int(input("Ingrese el dia "))
        mes= int(input("Ingrese el mes "))
        anio= int(input("Ingrese el anio "))
        print("Ingrese la segunda fecha")
        dia2= int(input("Ingrese el dia "))
        mes2= int(input("Ingrese el mes "))
        anio2= int(input("Ingrese el anio "))
        print(difFechas(dia,mes,anio,dia2,mes2,anio2))
    except:
        print("Respuesta invalida")


else:
    print("Respuesta invalida")