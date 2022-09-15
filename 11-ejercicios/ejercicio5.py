""" 
Ejercicio 5.
Crear una lista con el contenido de esta tabla:
ACCION      AVENTURA            DEPORTES
GTA         ASSASINS            FIFA 21
COD         CRASH               PRO 21
PUGB        Prince of persia    MOTO GP 21

Mostrar esta información ordenada
"""

tabla = [
    {
        "categoria": "ACCION",
        "juegos": ["GTA", "COD", "PUGB"]
    },
    {
        "categoria": "AVENTURA",
        "juegos": ["ASSASINS", "CRASH", "Prince of persia"]
    },
    {
        "categoria": "DEPORTES",
        "juegos": ["FIFA 21", "PRO 21", "MOTO GP 21"]
    }
]

for categoria in tabla:
    print("-"*5, f"{categoria['categoria']}", "-"*5)
    for juego in categoria['juegos']:
        print(juego)