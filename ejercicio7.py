
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

def esbisiesto(anio):
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

def diasenmes(mes):
    if esbisiesto(anio) == 1:
        dias["2"] = 29
        #si el año es bisiesto febrero ( que es 2 ) va a tener 29 dias
    return dias[str(mes)]
    # llama al diccionario dias definido previamente
# cuantos dias hay en el mes

def fechavalida(dia,mes,anio):
    if dia == "" or mes == "" or anio == "":
        return 0
    elif dia > 0:
        if 0 < mes and mes < 13:
            if dia > diasenmes(mes):
                return 0
            else:
                return 1
        else:
            return 0
    else:
        return 0
# validar fecha

def faltan(dia,mes,anio):
    if fechavalida(dia,mes,anio) == 0:
        return "Fecha no valida"
    elif fechavalida(dia,mes,anio) == 1:
        faltandias = diasenmes(mes) - (dia)
        return faltandias
"""  primero valida que la fecha sea valida y despues difdias el dia que es "dia" a la cantidad de dias que tiene el mes "diasenmes(mes)"
dias para que termine el mes """

def diashastafindeaño(dia,mes,anio):
    if fechavalida(dia,mes,anio) == 1:
        mesRestan = 12 - mes
        Diasrestantes=0
        if mesRestan != 0:
            for i in (range(mes, 12)):     
                auxiliar = diasenmes(i+1)  
                Diasrestantes = Diasrestantes + auxiliar  
        faltandias = Diasrestantes + faltan(dia,mes,anio)
        return faltandias
    else:
        return "Fecha no valida"
# dias para que termine el anio

def diastranscurridos(dia,mes,anio):
    if fechavalida(dia,mes,anio) == 1:
        diastrans=0
        if esbisiesto(anio) == 1:
            diastrans = 366 - diashastafindeaño(dia,mes,anio)
        elif esbisiesto(anio) == 0:
            diastrans = 365 - diashastafindeaño(dia,mes,anio)
        return diastrans
    else:
        return "Fecha no valida"
# dias trancurridos del anio

def difFechas(dia,mes,anio,dia2,mes2,anio2):
    if fechavalida(dia,mes,anio) == 1 or fechavalida(dia2,mes2,anio2) == 1:
        difdias = diastranscurridos(dia2,mes2,anio2) + diashastafindeaño(dia,mes,anio)
        anios = anio2 - anio
        aniosquepasaron = 0
        meses = 0
        dias = 0
        if anios == 0:
            difdias = 365 - (diashastafindeaño(dia2, mes2, anio2) + diastranscurridos(dia, mes,anio))
            while difdias != 0:
                if difdias - 30 >= 0:
                    difdias = difdias - 30
                    meses = meses + 1
                elif difdias - 1 >= 0:
                    difdias = difdias - 1
                    dias = dias + 1
            return (f"entre la fecha {dia}/{mes}/{aniosquepasaron} y {dia2}/{mes2}/{anio2} hay {dias} dias y {meses} meses")
        else:
            for i in range(1,anios):
                difdias = difdias + 365
            while difdias != 0:
                if difdias - 365 >= 0:
                    difdias = difdias - 365
                    aniosquepasaron = aniosquepasaron+ 1
                elif difdias - 30 >= 0:
                    difdias = difdias - 30
                    meses = meses + 1
                elif difdias - 1 >= 0:
                    difdias = difdias - 1
                    dias = dias + 1
            return (f"entre la fecha {dia}/{mes}/{anio} y {dia2}/{mes2}/{anio2} hay {dias} dias, {meses} meses y {aniosquepasaron} anios")
    else:
        return "Fecha invalida"
# diferencia entre dos fechas dadas por el usuario

# En todas las funciones hay un try, except que no permite al usuario completar campos con strings o dejar campo vacio
if func == 1:
    try:
        anio = int(input("ingrese el anio "))

        if esbisiesto(anio) == 1:
            print(f"el anio {anio} es bisiesto")

        elif esbisiesto(anio) == 0:
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

        if fechavalida(1,int(mes),1) == 1:
            print(f"Tiene {diasenmes(int(mes))} Dias")
        else:
            print("Mes no valido")

    except:
        print("Respuesta invalida")

elif func == 3: 
    try:
        dia= (int(input("Ingrese el dia ")))
        mes= (int(input("Ingrese el mes ")))
        anio= (int(input("Ingrese el anio ")))
        if fechavalida(dia,mes,anio) == 1:
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
        print(diashastafindeaño(dia,mes,anio))
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