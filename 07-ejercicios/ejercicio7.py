"""
Ejercicio 7. Hacer un programa que muestre todos los números impares
entre dos números que decida el usuario
"""

numero1 = int(input("Introduce un número: "))
numero2 = int(input("Introduce el siguiente número: "))

if numero1 < numero2:

    for x in range(numero1, (numero2 + 1)):

        if x % 2 == 0:
            print(f"{x} es PAR")
        else:
            print(f"{x} es IMPAR")

else:
    print("El némero 1 debe ser mayor al 2")
