from gestion import zoologico

class Zona:
    def __init__(self, nombre, zoo None, animales = None):
        self.nombre = nombre
        self.zoo = zoo
        self.animales = animales
    
    def Zona(self, nombre, zoo):
        self.nombre = nombre
        self.zoo = zoo

    def setNombre(self, nombre):
        self.nombre=nombre
    
    def getNombre(self):
        return self.nombre
        
    def setZoo(self, zoo):
        self.zoo = zoo
        
    def getZoo(self):
        return self.zoo
        
    def agregarAnimales(self, animal):
        self.animales.add(animal)
        
    def cantidadAnimales(self):
        return self.animales.size()
