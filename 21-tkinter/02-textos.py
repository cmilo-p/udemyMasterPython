from tkinter import *

ventana = Tk()
ventana.geometry("700x500")


texto = Label(ventana, text="Bienvenido a mi programa")
texto.config(
    fg="white",
    bg="#000000",
    padx=50,
    pady=20,
    font=("Consolas", 30)
)

def pruebas(nombre, apellidos, pais):
    return f"Hola {nombre} {apellidos} veo que eres de {pais}"

texto.pack()

texto = Label(ventana, text=pruebas(pais="Colombia", nombre="Camilo", apellidos="Pinzón"))
texto.config(
    height=3,
    bg="green",
    font=("Arial", 18),
    padx=10,
    pady=20,
    cursor="spider"
)
texto.pack(anchor=NW)

ventana.mainloop()
