class Coche:

    # Atributos o propiedades (variables)
    # Caracterirsticas del coche
    color = "Rojo"
    marca = "Ferrari"
    modelo = "Aventador"
    velocidad = 300
    caballaje = 500
    plazas = 2

    publico = "atributo publico"
    __privado = "atributo privado"

    def __init__(self, color, marca, modelo, velocidad, caballaje, plazas):
        self.color = color
        self.marca = marca
        self.modelo = modelo
        self.velocidad = velocidad,
        self.caballaje = caballaje
        self.plazas = plazas

    # Métodos, son acciones que hace el objeto (coche) (funciones)

    def getPrivado(self):
        return self.__privado

    def setColor(self, color):
        self.color = color

    def getColor(self):
        return self.color

    def setModel(self, modelo):
        self.modelo = modelo
    
    def getModelo(self):
        return self.modelo

    def setMarca(self):
        self.marca = self
    
    def getMarca(self):
        return self.marca

    def acelerar(self):
        self.velocidad += 1

    def frenar(self):
        self.velocidad -= 1

    def getVelocidad(self):
        return self.velocidad
    
    def getInfo(self):

        info = "----- Información del Coche -----"
        info += "\n Color: " + self.getColor()
        info += "\n Marca: " + self.getMarca()
        info += "\n Modelo: " + self.getModelo()
        info += "\n Velocidad: " + str(self.getVelocidad())

        return info

# fin definición clase
