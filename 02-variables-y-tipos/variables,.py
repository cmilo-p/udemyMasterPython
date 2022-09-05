""" 
Una variable es un contenedor de infromación
que desntro guardará un dato, se pueden crear
muchas variables y que cada una tenga una dato distinto.
"""

# Crear variables y asignarles un valor
texto = "Máster en Python"
texto2 = "con Victor Robles"
numero = 45
decimal = 6.7

# Mostrar valor de la variables
print(texto)
print(texto2)
print(numero)
print(decimal)

print("-"*25)

# Sustituir el valor de algunas variables / reasignar valores
numero = 77
decimal = 8.9
print(numero)
print(decimal)

print("-"*25)

# Concatenación
nombre = "Camilo"
apellidos = "Pinzón"
web = "VictorRoblesWeb.es"


print(nombre + " " + apellidos + " - " + web)
print(f"{nombre} {apellidos} - {web}")
print("Hola me llamo {} {} y mi web es: {}".format(nombre, apellidos, web))

print(nombre, apellidos, web)
