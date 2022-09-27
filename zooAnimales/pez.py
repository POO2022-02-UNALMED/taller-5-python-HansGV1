from gestion import zoologico
from zooAnimales import mamifero
from zooAnimales import ave
from zooAnimales import pez
from zooAnimales import reptil
from zooAnimales import anfibio

class Pez:
    def __init__(self, pez, salmones, bacalaos, colorEscamas, cantidadAletas, numpez): 
        self.pez = pez
        self.salmones = salmones
        self.bacalaos = bacalaos
        self.colorEscamas = colorEscamas
        self.cantidadAletas = cantidadAletas
        self.numpez = numpez
        
    def pez(self, nombre, edad,habitat, genero, colorEscamas, aletas):
        self.colorEscamas=colorEscamas
        self.cantidadAletas=aletas
        zoologico.setNombre(nombre)
        zoologico.setEdad(edad)
        zoologico.setHabitat(habitat)
        zoologico.setGenero(genero)
    
    def pez(self):
        self.numpez += 1
    
    def movimiento():
        return "nadar"
    
    def crearSalmon(self, nombre, edad, genero):
        self.pez.add(pez(nombre,edad,"oceano",genero,"rojo",6))
        self.salmones += 1
        self.numpez += 1
        return self.pez.get(self.pez.size()-1)
    
    def crearBacalao(self, nombre, edad, genero):
        self.pez.add(pez(nombre,edad,"oceano",genero,"gris",6))
        self.bacalaos += 1
        self.numpez += 1
        return self.pez.get(self.pez.size()-1)
    
    def cantidadPeces(self):
        return self.numpez
    
    def getColorEscamas(self):
        return self.colorEscamas
    
    def getCantidadAletas(self):
        return self.cantidadAletas
