"""
Proyecto Python y MySQL:
- Abrir asistente
- Login o registro
- Si elegimos registro, creará un usuarioen la bbdd
- Si elegimos login, identifica al usuario y nos preguntará
- Crear nota, mostrar, notas, borralas.
"""
from usuarios import acciones


print("""
Acciones disponibles:
    - registro
    - login
""")


hazEl = acciones.Acciones()
accion = input("¿Que quieres hacer?: ")

if accion == "registro":
    hazEl.resgistro()

elif accion == "login":
    hazEl.login()
