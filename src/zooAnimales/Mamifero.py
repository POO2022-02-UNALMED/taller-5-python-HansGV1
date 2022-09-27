from gestion import Zoologico
from zooAnimales import Mamifero
from zooAnimales import Ave
from zooAnimales import Pez
from zooAnimales import Reptil
from zooAnimales import Anfibio

class Mamifero:
    def __init__(self, mamifero, caballos, leones, pelaje, patas, numMamiferos):
        self.mamifero = mamifero
        self.caballos = caballos
        self.leones = leones
        self.pelaje = pelaje
        self.patas = patas
        self.numMamiferos = numMamiferos
        
    def Mamifero(self, nombre, edad,habitat, genero, pelaje, patas):
        self.patas= patas
        self.pelaje = pelaje
        Zoologico.setNombre(nombre)
        Zoologico.setEdad(edad)
        Zoologico.setHabitat(habitat)
        Zoologico.setGenero(genero)
    
    def Mamifero(self):
        self.numMamiferos += 1
    
    def cantidadMamiferos(self):
        return self.numMamiferos
    
    def crearCaballo(self, nombre, edad, genero):
        self.mamifero.add(Mamifero(nombre,edad,"pradera",genero,True,4))		
        self.numMamiferos += 1
        self.caballos+= 1	
        return self.mamifero.get(self.mamifero.size()-1)		
    
    def crearLeon(self, nombre, edad, genero):
        self.mamifero.add(Mamifero(nombre,edad,"selva",genero,True,4))
        self.numMamiferos += 1
        self.leones += 1
        return self.mamifero.get(self.mamifero.size()-1)
    
    def isPelaje(self):
        return self.pelaje
    
    def getPatas(self):
        return self.patas