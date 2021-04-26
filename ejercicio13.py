""" . Escribir un programa que compare dos strings y devuelva True si el primero es la versión capitalizada del segundo.

Nota: Por ejemplo, la versión capitalizada de la palabra “programar” es “PROGRAMAR”. """


palabra = input("ingrese una palabra: ")
palabra2 = input("ingrese otra palabra: ")
def verificarCapital(str1,str2):
    if palabra == palabra2.upper():
        return True
    else: 
        return False
if verificarCapital(palabra,palabra2):
    print(f"La palabra {palabra} es la version capitalizada de {palabra2}")
else:
    print(f"La palabra {palabra} no es la version capitalizada de palabra {palabra2}")
