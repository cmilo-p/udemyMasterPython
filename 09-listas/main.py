"""
LISTAS (arrays)
Son colecciones o conjuntos de datos/valores, bajo un unico
nombre.
Para acceder a esos valores podemos usar un indice númerico
"""

from operator import index


pelicula = "Batman"

# Definir lista
peliculas = ["Batma", "Spiderman", "El señor de los anillos"]
cantantes = list(('2pac', 'Drake', 'Jennifer Lopez'))
years = list(range(2020, 2050))
variada = ["Camilo", 30, 4.4, True, "texto"]
""" 
print(peliculas)
print(cantantes)
print(years)
print(variada)
 """

# Indices
pelicula = "otra cosa"
peliculas[1] = "Gran Torino"
peliculas[2] = "El hobbit"
print(peliculas)

print(peliculas[1])
print(peliculas[-2])
print(cantantes[1:3])
print(peliculas[2:])

# Añadir elementos a lista
cantantes.append("Kase O")
cantantes.append("Natos y waor")
print(cantantes)

# Recorrer lista
""" 
nueva_pelicula = ""
while nueva_pelicula != "parar":
    nueva_pelicula = input("Introduce la nueva pelicula: ")

    if nueva_pelicula != "parar":
        peliculas.append(nueva_pelicula)

print("\n", "*" * 5, "LISTADO PELICULAS", "*" * 5)
for pelicula in peliculas:
    print(f"{peliculas.index(pelicula)+1}. {pelicula}")
 """

# Listas multidimensionales
print("\n", "*" * 5, "LISTADO de contactos", "*" * 5)
contactos = [
    [
        'Antonio',
        'antonio@antonio.com'
    ],
    [
        'Luis',
        'luis@luis.com'
    ],
    [
        'Salvador',
        'salvador@salvador.com'
    ]
]

for contacto in contactos:
    for elemento in contacto:
        if contacto.index(elemento) == 0:
            print("Nombre: " + elemento)
        else:
            print("Email: " + elemento)
    print("\n")
        

#print(contactos[1][1])