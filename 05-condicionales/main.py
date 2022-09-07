"""
# Condicional IF

Si se_cumple_esta_condición:
    Ejecutar grupo de instrucciones
SI NO
    Se Ejecutan otro grupo de instrucciones

if condicion:
    instrucciones
else:
    otras instrucciones


# Operadores de comparación
== igual
!= diferente
< menor que
> mayor que
<= menor o igual que
>= mayor o igual que

# Operadores logicos
and Y
or O
! negacion
not NO

"""
# Ejemplo 1
print("#" * 10, "EJEMPLO 1", "#" * 10)

color = "rojo"
#color = input("Adivina cual es mi color favorito: ")

if color == "rojo":
    print("Enhorabuena!!")
    print("El color es ROJO")
else:
    print("Color incorrecto!!")


# Ejemplo 2
print("\n", "#" * 10, "EJEMPLO 2", "#" * 10)

year = 2020
# year = int(input("¿En que año estamos? "))

if year < 2021:
    print("Estamos antes de 2021 !!")
else:
    print("Es un año posterior al 2021")


# Ejemplo 3
print("\n", "#" * 10, "EJEMPLO 3", "#" * 10)

nombre = "Camilo Pinzón"
ciudad = "Bogotá"
continente = "America"
edad = 24
mayoria_edad = 18

if edad >= mayoria_edad:
    # Instrucciones
    print(f"{nombre} es mayor de edad")

    if continente != "Europa":
        print("El usuario no es Europeo")
    else:
        print(f"Es Europeo y de {ciudad}")

else:
    print(f"{nombre} NO es mayor de edad")

# Ejemplo 4
print("\n", "#" * 10, "EJEMPLO 4", "#" * 10)

dia = 2
# dia = int(input("Introduce el número del día de la semana: "))

""" 
if dia == 1:
    print("Es lunes")
else:
    if dia == 2:
        print("Es martes")
    else:
        if dia == 3:
            print("Es miercoles")
        else:
            if dia == 4:
                print("Es jueves")
            else:
                if dia == 5:
                    print("Es viernes")
                else:
                    print("Es fin de semana")
"""
if dia == 1:
    print("Es lunes")
elif dia == 2:
    print("Es martes")
elif dia == 3:
    print("Es miercoles")
elif dia == 4:
    print("Es jueves")
elif dia == 5:
    print("Es viernes")
else:
    print("Es fin de semana")


# Ejemplo 5
print("\n", "#" * 10, "EJEMPLO 5", "#" * 10)

edad_minima = 18
edad_maxima = 65
# edad_oficial = int(input("¿Tienes edad de trabajar? Introduce tu edad: "))
edad_oficial = 18

if edad_oficial >= 18 and edad_oficial <= 65:
    print("Esta en edad de trabajar !!")
else:
    print("No está en edad de trabajar")


# Ejemplo 6
print("\n", "#" * 10, "EJEMPLO 6", "#" * 10)

pais = "Rusia"

if pais == "Mexico" or pais == "España" or pais == "Colombia":
    print(f"{pais} es un pais de habla hispana !!")
else:
    print(f"{pais} NO es un pais de habla hispana :(")


# Ejemplo 7
print("\n", "#" * 10, "EJEMPLO 7", "#" * 10)

pais = "España"

if not (pais == "Mexico" or pais == "España" or pais == "Colombia"):
    print(f"{pais} NO es un pais de habla hispana :(")
else:
    print(f"{pais} SI un pais de habla hispana !!")


# Ejemplo 8
print("\n", "#" * 10, "EJEMPLO 8", "#" * 10)

pais = "USA"

if pais != "Mexico" and pais != "España" and pais != "Colombia":
    print(f"{pais} NO es un pais de habla hispana !!")
else:
    print(f"{pais} SI un pais de habla hispana :)")
