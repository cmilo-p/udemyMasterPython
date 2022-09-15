"""
Una función es un conjunto de instrucciones agrupadas bajo
un nombre concreto que pueden reutilizarseinvocando a 
la función tantas veces como sea necesario

def nombreDeMiFuncion(parametros):
    #BLOQUE / CONJUNTO DE INSTRUCCIONES

nombreDeMiFuncion(mi_parametro)
nombreDeMiFuncion(mi_parametro)

"""

# Ejemplo 1
print("#" * 10, "EJEMPLO 1", "#" * 10)

# Definir función


def muestraNombre():
    print("Camilo")
    print("Paco")
    print("Francisco")
    print("Aitor")
    print("Nestor")
    print("\n")


# Invocar función
muestraNombre()
muestraNombre()
muestraNombre()

# Ejemplo 2: Parametros
"""
print("\n", "#" * 10, "EJEMPLO 2", "#" * 10)


def mostrarTuNombre(nombre, edad):
    print(f"Tu nombre es: {nombre}")

    if edad >= 18:
        print("Y eres mayor de edad")


nombre = input("Introduce tu nombre: ")
edad = int(input("Introduce tu edad: "))
mostrarTuNombre(nombre, edad)
"""

# Ejemplo 3
print("\n", "#" * 10, "EJEMPLO 3", "#" * 10)


def tabla(numero):
    print(f"Tabla de multiplicar del número: {numero}")

    for contador in range(11):
        operacion = numero * contador
        print(f"{numero} x {contador} = {operacion}")

    print("\n")


tabla(3)
tabla(7)
tabla(12)

# Ejemplo 3.1
print("-" * 30)

for numero_tabla in range(1, 11):
    tabla(numero_tabla)

# Ejemplo 4
print("\n", "#" * 10, "EJEMPLO 4", "#" * 10)

# Parametros opcionales


def getEmpleado(nombre, dni=None):
    print("EMPLEADO")
    print(F"Nombre: {nombre}")

    if dni != None:
        print(F"DNI: {dni}")


getEmpleado("Camilo", 12345)

# Ejemplo 5: return o devolver datos
print("\n", "#" * 10, "EJEMPLO 5", "#" * 10)


def saludame(nombre):
    saludo = f"Hola, saludos {nombre}"

    return saludo


print(saludame("Camilo"))

# Ejemplo 6
print("\n", "#" * 10, "EJEMPLO 6", "#" * 10)


def calculadora(numero1, numero2, basicas=False):

    suma = numero1 + numero2
    resta = numero1 - numero2
    multi = numero1 * numero2
    division = numero1 / numero2

    cadena = ""

    if basicas != False:
        cadena += "Suma: " + str(suma)
        cadena += "\n"
        cadena += "Resta: " + str(resta)
    else:
        cadena += "Multiplicación: " + str(multi)
        cadena += "\n"
        cadena += "Division: " + str(division)

    return cadena


print(calculadora(56, 5, True))

# Ejemplo 7
print("\n", "#" * 10, "EJEMPLO 7", "#" * 10)


def getNombre(nombre):
    texto = f"El nombre es: {nombre}"
    return texto


def getApellidos(apellidos):
    texto = f"Los apellidos son: {apellidos}"
    return texto


def devuelveTodo(nombre, apellidos):
    texto = getNombre(nombre) + "\n" + getApellidos(apellidos)
    return texto


print(devuelveTodo("Camilo", "Pinzón"))

# Ejemplo 8: Funciones lambda (Funciones anonimas)
""" Sirve para tareas cortas, debe definirse en una linea """
print("\n", "#" * 10, "EJEMPLO 8", "#" * 10)


def dime_el_year(year): return f"El año es {year * 50}"


print(dime_el_year(2034))
