"""
Ejercicio 5. Hacer un programa que muestren todos los números entre
dos numeros que diga el usuario.
"""

numero1 = int(input("Introduce el primer número: "))
numero2 = int(input("Introduce el segundo número: "))

if numero1 < numero2:

    for contador in range(numero1, (numero2 + 1)):
        print(contador)

else:
    print("el número 1 debe ser menor al número 2")
