""" Escribir una función que dada la cantidad de ejercicios de un examen, 
y el porcentaje necesario de ejercicios bien resueltos necesario para aprobar dicho examen,
revise un grupo de exámenes. Para ello, en cada paso debe preguntar la cantidad de ejercicios resueltos
por el alumno, indicando con un valor centinela que no hay más exámenes a revisar.
Debe mostrar por pantalla el porcentaje correspondiente a la cantidad de ejercicios resueltos 
respecto a la cantidad de ejercicios del examen y una leyenda que indique si aprobó o no. """


import helper


def aprobo(porcentaje): 
    """     Recibe:
            porcentaje:<int>
    dice si aprobo o no  """
    if porcentaje > nota or porcentaje == nota:
        return 1
    else:
        return 0   


while True: # pide los datos y dice si aprobo o no y con cuanto
    try:
        examen = int(input("ingrese la cantidad de ejercicios que tiene el examen: "))
        nota = int(input("¿Con que porcentaje aprobara? "))
        ejercicios = int(input("¿Cuantos ejercicios resolvio correctamente? "))
        porcentaje = (100/examen)*ejercicios


        if aprobo(porcentaje) == 1:
            print(f"El alumno aprobo con un {porcentaje}%")
            break
        else:
            print(f"El alumno desaprobo con un {porcentaje}%")
            break
    except ValueError:
        print("porfavor ingrese valores numericos")
        continue


