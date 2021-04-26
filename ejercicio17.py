""" 17. Procesamiento de telegramas. Un oficial de correos decide optimizar el trabajo de su
oficina cortando todas las palabras de más de cinco letras a sólo cinco letras (e indicando
que una palabra fue cortada con el agregado de una arroba). Además elimina todos los
espacios en blanco de más. Por ejemplo, al texto " Llego mañana alrededor del mediodía "
se transcribe como "Llego mañan@ alred@ del medio@". Por otro lado cobra un valor para
las palabras cortas y otro valor para las palabras largas (que deben ser cortadas).
    1. Escribir una función que reciba un texto, la longitud máxima de las palabras, el costo de
    cada palabra corta, el costo de cada palabra larga, y devuelva como resultado el texto del
    telegrama y el costo del mismo.
    2. Los puntos se reemplazan por la palabra especial ”STOP”, y el punto final (que puede
    faltar en el texto original) se indica como ”STOPSTOP”. Al texto: 
    " Llego mañana alrededor del mediodía. Voy a almorzar " Se lo transcribe como: "Llego mañan@
    alred@ del medio@ STOP Voy a almor@ STOPSTOP". """

texto = input("ingrese el telegrama: ")
maxLetras= int(input("Ingrese el maximo de letras por palabra: "))
costoC= float(input("Ingrese el costo de las palabras cortas: "))
costoL= float(input("Ingrese el costo de las palabras largas: "))
pLarga = 0
pCorta = 0
telegrama = ""

def longmax(texto,pLarga,pCorta,telegrama):
    costo = 0
    palabras = texto.split(" ")
    # divido el texto por " " en una lista llamada palabras
    palabras[-1] = palabras[-1].rstrip(".")
    # saco el punto del final en el caso de que haya para luego reemplazarlo por STOPSTOP y que no queden tres STOP
    for i in range(len(palabras)):    
        aux = palabras[i]
        # aux Es un auxiliar que me sirve para no tener que llamar a la lista todo el tiempo
        if (len(aux)) >= maxLetras:
            pLarga = pLarga + 1
        elif (len(aux)) < maxLetras:
            pCorta = pCorta + 1
        costo = (costoC*pCorta) + (costoL*pLarga)
        # En esta parte calculo el coste en base a la cantidad de palabras largas o cortas multiplicadas
        # por su coste
        B = 0
        for letra in aux:
            if letra in ".":
                B = 1
        # B Es un auxiliar que me sirve para saber si la palabra va a tener que tener un STOP al final
        if len(aux)>maxLetras and B == 1:
            aux = aux[0:maxLetras] + "@ " + "STOP"
        elif len(aux)>maxLetras and B != 1:
            aux = aux[0:maxLetras] + "@"
        # En estos dos if le digo al programa que si supera la cantidad maxima reemplaze lo que sigue por @ y si 
        # el auxiliar B es 1 añada tambien un STOP
        telegrama = telegrama + aux + " "
    telegrama = telegrama.strip()  + "STOPSTOP"
    # Con strip borro los espacios del principio y del final y despues añado STOPSTOP al final indiscriminadamente
 
    print(f"El telegrama se vera asi ({telegrama}), tendra un costo de {costo} y tiene {pCorta} palabras cortas y {pLarga} palabras largas")

longmax(texto,pLarga,pCorta,telegrama)