""" 
Ejercicio 3. Escribir un programa que muestre los cuadrados
(un numero multiplicado por si mismo) de los 60 primeros números
naturales. Resolverlo con fir y con while
"""

# WHILE

from socket import NI_NUMERICHOST


"""
contador = 0
while contador <= 60:

    cuadrado = contador * contador
    print(f"El cuadrado de {contador} es {cuadrado}")

    contador += 1
"""

# FOR
for numero in range(61):
    cuadrado = numero * numero
    print(f"El cuadrado de {numero} es {cuadrado}")