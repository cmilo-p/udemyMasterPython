"""
Ejercicio 6. Mostrar todas las tablas de multiplicar del 1 al 10.
Mostrando el titulo de la tabla y luego las multiplicaciones del 1 al 10.
"""

for cabecera in range(1, 11):
    print("#" * 32)
    print("#" * 9, f"Tabla del {cabecera}", "#" * 9)
    print("#" * 32)

    for numero in range(1, 11):
        print(f"{numero} x {cabecera} = {numero * cabecera}")

    print("\n")