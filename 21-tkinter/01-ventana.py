# Tkinter
# Modulo para crear interfaces graficas de usuario

from tkinter import *
import os.path


class Programa:

    def __init__(self):
        self.title = "Master en Python"
        self.icon = "./imagenes/logotipo.ico"
        self.icon_alt = "./21-tkinter/imagenes/logotipo.ico"
        self.size = "770x470"
        self.resiable = False

    def cargar(self):
        # Crear la ventana raiz
        ventana = Tk()
        self.ventana = ventana

        # Titulo de la ventana
        ventana.title(self.title)

        # Comprobar si existe un archivo
        ruta_icono = os.path.abspath(self.icon)

        if not os.path.isfile(ruta_icono):
            ruta_icono = os.path.abspath(self.icon_alt)

        # Icono de la ventana
        ventana.iconbitmap(ruta_icono)

        # Mostrar texto en el programa
        texto = Label(ventana, text=ruta_icono)
        texto.pack()

        # Cambio en el tamaño de la ventana
        ventana.geometry(self.size)

        # Bloquear el tamaño de la ventana
        if self.resiable:
            ventana.resizable(1, 1)
        else:
            ventana.resizable(0, 0)

    def addTexto(self, dato):
        texto = Label(self.ventana, text = dato)
        texto.pack()

    def mostrar(self):
        # Arrancar mostar la ventana hasta que se cierre
        self.ventana.mainloop()

# Instanciar programa
programa = Programa()
programa.cargar()
programa.addTexto("Soy un texto")
programa.addTexto("Master Python")
programa.mostrar()