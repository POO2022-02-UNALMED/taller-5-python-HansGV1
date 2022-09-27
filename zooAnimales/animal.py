from gestion import zoologico
from zooAnimales import mamifero
from zooAnimales import ave
from zooAnimales import pez
from zooAnimales import reptil
from zooAnimales import anfibio

class Animal:
    def __init__(self, nombre=None, edad=0, habitat=None, genero=None):
        self.nombre = nombre
        self.edad = edad
        self.habitat = habitat
        self.genero = genero
    
    def Animal(self, nombre, edad, habitat, genero):		
        self.setNombre(nombre)
        self.setEdad(edad)
        self.setHabitat(habitat)
        self.setGenero(genero)
    
    def movimiento(): 
        return "desplazarse"
    
    def to(self): 
        return "Mi nombre es " + self.getNombre()+", tengo una edad de "+ self.getEdad()+", habito en "+self.getHabitat() +" y mi genero es "+self.getGenero()
    
    def totalPorTipo(self): 
        return  "Mamiferos: "+mamifero.cantidadMamiferos()+"\n"+ "Aves: "+ave.cantidadAves()+"\n"+"Reptiles: "+reptil.cantidadReptiles()+"\n"+"Peces: "+pez.cantidadPeces()+"\n"+"Anfibios: "+anfibio.cantidadAnfibios()+"\n"

    def getNombre(self): 
        return self.nombre
    
    def setNombre(self, nombre): 
        self.nombre = nombre
    
    def getEdad(self): 
        return self.edad
    
    def setEdad(self, edad): 
        self.edad = edad
    
    def getHabitat(self): 
        return self.habitat
    
    def setHabitat(self, habitat): 
        self.habitat = habitat
        
    def getGenero(self):
        return self.genero
    
    def setGenero(self, genero):
        self.genero = genero
