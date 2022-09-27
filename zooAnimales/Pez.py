from gestion import Zoologico
from zooAnimales import Mamifero
from zooAnimales import Ave
from zooAnimales import Pez
from zooAnimales import Reptil
from zooAnimales import Anfibio

class Pez:
    def __init__(self, pez, salmones, bacalaos, colorEscamas, cantidadAletas, numPez): 
        self.pez = pez
        self.salmones = salmones
        self.bacalaos = bacalaos
        self.colorEscamas = colorEscamas
        self.cantidadAletas = cantidadAletas
        self.numPez = numPez
        
    def Pez(self, nombre, edad,habitat, genero, colorEscamas, aletas):
        self.colorEscamas=colorEscamas
        self.cantidadAletas=aletas
        Zoologico.setNombre(nombre)
        Zoologico.setEdad(edad)
        Zoologico.setHabitat(habitat)
        Zoologico.setGenero(genero)
    
    def Pez(self):
        self.numPez += 1
    
    def movimiento():
        return "nadar"
    
    def crearSalmon(self, nombre, edad, genero):
        self.pez.add(Pez(nombre,edad,"oceano",genero,"rojo",6))
        self.salmones += 1
        self.numPez += 1
        return self.pez.get(self.pez.size()-1)
    
    def crearBacalao(self, nombre, edad, genero):
        self.pez.add(Pez(nombre,edad,"oceano",genero,"gris",6))
        self.bacalaos += 1
        self.numPez += 1
        return self.pez.get(self.pez.size()-1)
    
    def cantidadPeces(self):
        return self.numPez
    
    def getColorEscamas(self):
        return self.colorEscamas
    
    def getCantidadAletas(self):
        return self.cantidadAletas
