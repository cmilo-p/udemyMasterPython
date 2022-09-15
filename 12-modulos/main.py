""" 
Modulos: son funcionalidades ya hechas para reutilizar.

En python hay muchos modulos, que los puedes consultar aquí:
https://docs.python.org/es/3/tutorial/modules.html#

Podemos conseguir modulos que ya vienen en el lenguaje,
modulos en internet, y tambien podemos crear nuestros modulos
"""

# Importar modulo propio
#import mimodulo
#from mimodulo import holaMundo
from mimodulo import *

#print(mimodulo.holaMundo("Camilo Pinzón"))
#print(mimodulo.calculadora(3, 5, True))

print(holaMundo("Camilo Pinzón"))
print(calculadora(3, 5, True))
print("\n")

# Modulo de fechas
import datetime

print(datetime.date.today())

fecha_completa = datetime.datetime.now()
print(fecha_completa)
print(fecha_completa.year)
print(fecha_completa.month)
print(fecha_completa.day)

fecha_personalizada = fecha_completa.strftime("%d/%m/%Y, %H:%M:%S")
print("Mi fecha personalizada: ",fecha_personalizada)

print(datetime.datetime.now().time())
print("\n")

# Modulo matematicas
import math

print("Raiz cuadrada de 10: ", math.sqrt(10))

print("Número pi: ", float(math.pi))
print("Redondear: ", math.ceil(6.16798))
print("Redondear: ", math.floor(6.16798))
print("\n")

# Modulo random
import random

print("Número aleatorio entre 15 y 67: ", random.randint(15, 67))