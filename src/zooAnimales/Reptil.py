from gestion import zoologico
from zooAnimales import mamifero
from zooAnimales import ave
from zooAnimales import pez
from zooAnimales import reptil
from zooAnimales import anfibio

class Reptil:
    def __init__ (self, reptil, iguanas, serpientes, colorEscamas, largoCola, numreptil):
        self.reptil = reptil
        self.iguanas = iguanas
        self.serpientes = serpientes
        self.colorEscamas = colorEscamas
        self.largoCola = largoCola
        self.numreptil = numreptil
    
    def reptil(self, nombre, edad,habitat, genero, colorEscamas, cola):
        self.colorEscamas=colorEscamas
        self.largoCola=cola
        zoologico.setNombre(nombre)
        zoologico.setEdad(edad)
        zoologico.setHabitat(habitat)
        zoologico.setGenero(genero)
    
    def reptil(self):
        self.numreptil += 1
    
    def movimiento():
        return "reptar"
    
    def crearIguana(self, nombre, edad, genero):
        self.reptil.add(reptil(nombre,edad,"humedal",genero,"verde",3))
        self.numreptil += 1	
        self.iguanas += 1
        return self.reptil.get(self.reptil.size()-1)
    
    def crearSerpiente(self, nombre, edad, genero):
        self.reptil.add(reptil(nombre,edad,"jungla",genero,"blanco",1))
        self.numreptil += 1	
        self.serpientes += 1
        return self.reptil.get(self.reptil.size()-1)
    
    def cantidadreptiles(self):
        return self.numreptil
    
    def getColorEscamas(self):
        return self.colorEscamas
    
    def getLargoCola(self):
        return self.largoCola
