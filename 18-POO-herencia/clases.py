# HERENCIA: Es la posibilidad de compartir atributos y métodos
# entre clases. Y que diferentes clases hereden de otras

class Persona:
    """
    nombre
    apellidos
    altura
    edad
    """

    def getNombre(self):
        return self.nombre

    def getApellidos(self):
        return self.apellidos

    def getAltura(self):
        return self.altura

    def getEdad(self):
        return self.edad

    def setNombre(self, nombre):
        self.nombre = nombre

    def setApellidos(self, apellidos):
        self.apellidos = apellidos

    def setAltura(self, altura):
        self.altura = altura

    def setEdad(self, edad):
        self.edad = edad

    def hablar(self):
        return "Hablando..."

    def caminar(self):
        return "caminando..."

    def dormir(self):
        return "durmiendo."


class Informatico(Persona):
    """
    lenguajes
    experiencia
    """

    def __init__(self):
        self.lenguajes = "HTML, CSS, Javascript, PHP"
        self.experiencia = 5
        #super().__init__()

    def getLenguajes(self):
        return self.lenguajes

    def aprender(self, lenguajes):
        self.lenguajes = lenguajes
        return self.lenguajes

    def programar(self):
        return "Programando..."

    def repararPC(self):
        return "Ordenador reparado"

class TecnicoRedes(Informatico):
    
    def __init__(self):
        super().__init__()
        self.auditarRedes = "experto"
        self.experienciaRedes = 15
        
    def auditoria(self):
        return "Auditando red..."
