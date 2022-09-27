from gestion import Zoologico
from zooAnimales import Mamifero
from zooAnimales import Ave
from zooAnimales import Pez
from zooAnimales import Reptil
from zooAnimales import Anfibio

class Reptil:
    def __init__ (self, reptil, iguanas, serpientes, colorEscamas, largoCola, numReptil):
        self.reptil = reptil
        self.iguanas = iguanas
        self.serpientes = serpientes
        self.colorEscamas = colorEscamas
        self.largoCola = largoCola
        self.numReptil = numReptil
    
    def Reptil(self, nombre, edad,habitat, genero, colorEscamas, cola):
        self.colorEscamas=colorEscamas
        self.largoCola=cola
        Zoologico.setNombre(nombre)
        Zoologico.setEdad(edad)
        Zoologico.setHabitat(habitat)
        Zoologico.setGenero(genero)
    
    def Reptil(self):
        self.numReptil += 1
    
    def movimiento():
        return "reptar"
    
    def crearIguana(self, nombre, edad, genero):
        self.reptil.add(Reptil(nombre,edad,"humedal",genero,"verde",3))
        self.numReptil += 1	
        self.iguanas += 1
        return self.reptil.get(self.reptil.size()-1)
    
    def crearSerpiente(self, nombre, edad, genero):
        self.reptil.add(Reptil(nombre,edad,"jungla",genero,"blanco",1))
        self.numReptil += 1	
        self.serpientes += 1
        return self.reptil.get(self.reptil.size()-1)
    
    def cantidadReptiles(self):
        return self.numReptil
    
    def getColorEscamas(self):
        return self.colorEscamas
    
    def getLargoCola(self):
        return self.largoCola
