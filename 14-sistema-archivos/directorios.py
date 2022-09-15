import os
import shutil

# Crear carpeta
if not os.path.isdir("./14-sistema-archivos/mi_carpeta"):
    os.mkdir("./14-sistema-archivos/mi_carpeta")
else:
    print("Ya existe el directorio")

# Copiar
"""
ruta_original = "./14-sistema-archivos/mi_carpeta"
ruta_nueva = "./14-sistema-archivos/mi_carpeta_COPIADA"

shutil.copytree(ruta_original, ruta_nueva)
"""

# Eliminar 
"""
os.rmdir("./14-sistema-archivos/mi_carpeta_COPIADA")
"""

print("Contenido de mi carpeta:")
contenido = os.listdir("./14-sistema-archivos/mi_carpeta")

for fichero in contenido:
    print("Fichero" + fichero)