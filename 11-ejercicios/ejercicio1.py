""" 
Ejercicio 1. Hacer un programa que tenga una lista
de 8 números enteros y haga los siguiente:
- Recorrer la lista y mostrarla
- Hacer funcion que recorra listas de numeros y devuelva un string
- Ordenarla y mostrarla
- Mostrar su longitud
- Buscar algun elemento (que el usuario pida por teclado)
"""

# Crear lista
from re import search


numeros = [13, 64, 52, 73, 21, 7, 91, 63]

# Crear funcion que recorra listas y devuelva string


def mostrarLista(lista):
    resultado = ""

    for elemento in lista:
        resultado += "Elemento: " + str(elemento)
        resultado += "\n"

    return resultado


# Recorrer y mostrar
print("##### Recorrer y mostrar #####")

""" 
for numero in numeros:
    print(numero) 
"""

print(mostrarLista(numeros))
print(mostrarLista(numeros))
print(mostrarLista(["Victor", "Juan", "Pepe"]))

# Ordenar y mostar
print("##### Ordenar y mostar #####")
numeros.sort()
print(mostrarLista(numeros))

# Mostrar logitud
print("##### Mostrar logitud #####")
print(len(numeros))

# Busqueda en la lista
try:
    print("##### Busqueda en la lista #####")

    busqueda = int(input("Introduce el número: "))

    comprobar = isinstance(busqueda, int)
    while not comprobar or busqueda <= 0:
        busqueda = int(input("Introduce el número: "))
    else:
        print(f"Has introducido el {busqueda}")

    print(f"##### Buscar en la lista el número {busqueda} ##### ")

    search = numeros.index(busqueda)
    print(f"El número buscado existe en la lista, es el indice {search}")
except:
    print("El número no esta en la lista, lo siento !!")

