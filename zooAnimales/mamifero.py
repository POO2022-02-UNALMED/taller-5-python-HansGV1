from gestion import zoologico
from zooAnimales import mamifero
from zooAnimales import ave
from zooAnimales import pez
from zooAnimales import reptil
from zooAnimales import anfibio

class Mamifero:
    def __init__(self, mamifero, caballos, leones, pelaje, patas, nummamiferos):
        self.mamifero = mamifero
        self.caballos = caballos
        self.leones = leones
        self.pelaje = pelaje
        self.patas = patas
        self.nummamiferos = nummamiferos
        
    def mamifero(self, nombre, edad,habitat, genero, pelaje, patas):
        self.patas= patas
        self.pelaje = pelaje
        zoologico.setNombre(nombre)
        zoologico.setEdad(edad)
        zoologico.setHabitat(habitat)
        zoologico.setGenero(genero)
    
    def mamifero(self):
        self.nummamiferos += 1
    
    def cantidadmamiferos(self):
        return self.nummamiferos
    
    def crearCaballo(self, nombre, edad, genero):
        self.mamifero.add(mamifero(nombre,edad,"pradera",genero,True,4))		
        self.nummamiferos += 1
        self.caballos+= 1	
        return self.mamifero.get(self.mamifero.size()-1)		
    
    def crearLeon(self, nombre, edad, genero):
        self.mamifero.add(mamifero(nombre,edad,"selva",genero,True,4))
        self.nummamiferos += 1
        self.leones += 1
        return self.mamifero.get(self.mamifero.size()-1)
    
    def isPelaje(self):
        return self.pelaje
    
    def getPatas(self):
        return self.patas
