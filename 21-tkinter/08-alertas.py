from tkinter import *
from tkinter import messagebox as Messagebox

ventana = Tk()
ventana.config(bd=70)


def sacarAlerta():
    Messagebox.showerror("Alerta", "Hola es una alerta")


Button(ventana, text="Mostrar alerta!!", command=sacarAlerta).pack()


def salir(nombre):
    resultado = Messagebox.askquestion(
        "Salir", "¿Continuar ejecutando la aplicación?")

    if resultado != "yes":
        Messagebox.showinfo("Chao!!", f"Adios {nombre}")
        ventana.destroy()


# Con la función lambda se evita que se ejecuta la función salir hasta ante que se llame por medio del botón
Button(ventana, text="Salir", command=lambda: salir("Camilo Pinzón")).pack()

ventana.mainloop()
