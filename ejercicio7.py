
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
    """ eleccion de la funcion """ 
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
# tryexcept para que el usuario no use strings ni campo vacio


def esBisiesto(anio):
    """ Recibe:
            anio:<int>
    Indica si el año ingresado es bisiesto """
    if anio % 4 == 0 and anio % 100 == 0:
        if anio % 400 == 0:
            return 1
            # si el anio tiene que ser divisible por 4 y por 100 a menos que sea divisible por 400 no es bisiesto
        else:
            return 0
    else:
        if anio % 4 == 0:
            return 1
        # si el anio tiene que ser divisible solo por 4 es bisiesto
        else:
            return 0


def diasMes(mes):
    Recibe:
            mes:<int>
    indica cuantos dias hay en el mes
    if esBisiesto(anio) == 1:
        dias["2"] = 29
        #si el año es bisiesto febrero ( que es 2 ) va a tener 29 dias
    return dias[str(mes)]
    # llama al diccionario dias definido previamente


def fechaValida(dia,mes,anio): 
    """ Recibe:
            dia:<int>
            mes:<int>
            anio:<int>
    valida la fecha ingresada """
    if dia == "" or mes == "" or anio == "":
        return 0
    elif dia > 0:
        if 0 < mes and mes < 13:
            # el mes no tiene que ser mayor a 12 o menor que 0
            if dia > diasMes(mes):
                # los dias no tienen que ser mayor que los dias que tiene el mes ya sea 30, 31, 28 o 29
                return 0
            else:
                return 1
        else:
            return 0
    else:
        return 0



def faltan(dia,mes,anio):
    """ Recibe:
            dia:<int>
            mes:<int>
            anio:<int>
    Calcula los dias que faltan para que termine el mes """
    if fechaValida(dia,mes,anio) == 0:
        return "Fecha no valida"
    elif fechaValida(dia,mes,anio) == 1:
        faltandias = diasMes(mes) - (dia)
        return faltandias
    #  primero valida que la fecha sea valida y despues resta el dia que es "dia" a la cantidad de dias que tiene el mes "diasMes(mes)"
    


def diashastafindeaño(dia,mes,anio):
    """ Recibe:
            dia:<int>
            mes:<int>
            anio:<int>
    indica cuantos dias faltan para que termine el anio desde la fecha ingresada """
    if fechaValida(dia,mes,anio) == 1:
        mesRestan = 12 - mes
        # meses que le quedan al año 
        Diasrestantes=0
        if mesRestan != 0:
            for i in (range(mes, 12)):     
                auxiliar = diasMes(i+1)  
                Diasrestantes = Diasrestantes + auxiliar  
        faltandias = Diasrestantes + faltan(dia,mes,anio)
        # sumo los dias de cada mes que falta en el for y los dias restantes en el mes en el que se encuentran
        return faltandias
    else:
        return "Fecha no valida"


def diasTranscurridos(dia,mes,anio):
    """ Recibe:
            dia:<int>
            mes:<int>
            anio:<int>
    indica los dias trancurridos del anio hasta la fecha ingresada """
    if fechaValida(dia,mes,anio) == 1:
        diasTrans=0
        if esBisiesto(anio) == 1:
            diasTrans = 366 - diashastafindeaño(dia,mes,anio)
        elif esBisiesto(anio) == 0:
            diasTrans = 365 - diashastafindeaño(dia,mes,anio)
        return diasTrans
    else:
        return "Fecha no valida"
    # esta funcion funciona con la funcion diashastafindeaño restandosela a 365 para obtener lo contrario (los dias transcurridos)


def difFechas(dia,mes,anio,dia2,mes2,anio2):
    """ Recibe:
            dia:<int>
            mes:<int>
            anio:<int>
            dia2:<int>
            mes2:<int>
            anio2:<int>
    indica cuanta diferencia de dias hay entre dos fechas dadas por el usuario """
        if fechaValida(dia,mes,anio) == 1 or fechaValida(dia2,mes2,anio2) == 1:
            difDias = 0
            aniosEntreFechas = anio2 - anio
            
            aniosQuePasaron = 0
            meses = 0
            dias = 0

            if aniosEntreFechas == 0:
                difDias = 365 - (diashastafindeaño(dia2, mes2, anio2) + diasTranscurridos(dia, mes,anio)) + 1
                # Si la comparacion es en el mismo tendra que restar los dias que le quedan para terminar el año  a la segunda fecha y los dias transcurridos de la primera 
                # y añade 1 por que siempre va a dar la diferencia menos 1

            else:
                difDias = diasTranscurridos(dia2,mes2,anio2) + diashastafindeaño(dia,mes,anio)
                for i in range(1,aniosEntreFechas):
                    difDias = difDias + 365
                # si son años distintos tendra que sumas 365 por los años que hay en el medio y hacer los dias que le faltan para terminar el año a la primera fecha y los dias transcurridos de la segunda

            while difDias >= 30:
                    if difDias - 365 >= 0:
                        difDias = difDias - 365
                        aniosQuePasaron = aniosQuePasaron + 1
                    elif difDias - 30 >= 0 and difDias - 365 < 0:
                        difDias = difDias - 30
                        meses = meses + 1
            # siempre que pueda restar 365 sumara un año y lo restara y sino restara 30 y sumara 1 mes

            if meses == 12:
                meses = 0
                aniosQuePasaron =+ 1        
            # si hay 360 a 364 dias dira que hay 12 meses lo que sera un error por eso hay que cambiarlo a 1 anio

            if aniosEntreFechas == 0:
                return (f"Entre la fecha {dia}/{mes}/{anio} y {dia2}/{mes2}/{anio2} hay {difDias} dias y {meses} meses")
            else:
                return (f"Entre la fecha {dia}/{mes}/{anio} y {dia2}/{mes2}/{anio2} hay {difDias} dias, {meses} meses y {aniosQuePasaron} anios")
        else:
            return "Fecha invalida"


# En todas las funciones hay un try, except que no permite al usuario completar campos con strings o dejar campo vacio
if func == 1:
    try:
        anio = int(input("ingrese el anio "))

        if esBisiesto(anio) == 1:
            print(f"el anio {anio} es bisiesto")

        elif esBisiesto(anio) == 0:
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

        if fechaValida(1,int(mes),1) == 1:
            print(f"Tiene {diasMes(int(mes))} Dias")
        else:
            print("Mes no valido")

    except:
        print("Respuesta invalida")


elif func == 3: 
    try:
        dia= (int(input("Ingrese el dia ")))
        mes= (int(input("Ingrese el mes ")))
        anio= (int(input("Ingrese el anio ")))
        if fechaValida(dia,mes,anio) == 1:
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
        print(diasTranscurridos(dia,mes,anio))
    except:
        print("Respuesta invalida") 


elif func == 7:
        print("Ingrese la primera fecha")
        dia= int(input("Ingrese el dia "))
        mes= int(input("Ingrese el mes "))
        anio= int(input("Ingrese el anio "))
        print("Ingrese la segunda fecha")
        dia2= int(input("Ingrese el dia "))
        mes2= int(input("Ingrese el mes "))
        anio2= int(input("Ingrese el anio "))
        print(difFechas(dia,mes,anio,dia2,mes2,anio2))
    


else:
    print("Respuesta invalida")