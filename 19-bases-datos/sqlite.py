# Importar modulo
import sqlite3

# Conexion
conexion = sqlite3.connect('19-bases-datos\pruebas.db')

# Crear cursor
cursor = conexion.cursor()

# Crear tabla
"""cursor.execute(CREATE TABLE IF NOT EXISTS productos(
id INTEGER PRIMARY KEY AUTOINCREMENT,
titulo VARCHAR(255),"
descripcion text,"
precio int(255)"
))"""

# Guardar cambios
conexion.commit()

# Insertar datos
""" 
cursor.execute("INSERT INTO productos VALUES(null, 'Segundo producto', 'Descripción de mi producto', 550)")
conexion.commit()
"""

# Borrar registros
cursor.execute("DELETE FROM productos")
conexion.commit()

# Insertar muchos registros de golpe
productos = [
    ("Ordenador portatil", "Buen PC", 700),
    ("Telefono movil", "Buen Telefono", 140),
    ("Placa base", "Buena placa", 80),
    ("Tablet 15", "Buen tablet", 300),
]
cursor.executemany("INSERT INTO productos VALUES (null, ?, ?, ?)", productos)
conexion.commit()

# Update
cursor.execute("UPDATE productos SET precio = 678 WHERE precio = 80")

# Listar datos
cursor.execute("SELECT * FROM productos WHERE precio >= 300;")
productos = cursor.fetchall()

for producto in productos:
    print("ID: ", producto[0])
    print("Titulo: ", producto[1])
    print("Descripción: ", producto[2])
    print("precio: ", producto[3])
    print("\n")


cursor.execute("SELECT titulo FROM productos;")
producto = cursor.fetchone()
print(producto)

# Cerrar conexión
conexion.close()
