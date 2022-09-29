from zooAnimales.anfibio import Anfibio
from zooAnimales.pez import Pez
from zooAnimales.reptil import Reptil
from zooAnimales.ave import Ave
from zooAnimales.mamifero import Mamifero
from gestion.zoologico import Zoologico

class Animal:
    def __init__(self,totalAnimales, nombre, edad, habitat, genero, zona):
        self._totalAnimales = totalAnimales
        self._nombre = nombre
        self._edad = edad
        self._habitat = habitat
        self._genero = genero
        self._zona = zona
  
    def getTotalAnimales (self):
        return self._totalAnimales
    
    def setAnimales(self):
        self._totalAnimales = Mamifero.cantidadMamiferos() + Ave.cantidadAves() + Reptil.cantidadReptiles() + Pez.cantidadPeces() + Anfibio.cantidadAnfibios()
                
    def getNombre (self):
        return self._nombre
    
    def setNombre (self, nom):
        self._nombre = nom
        
    def getEdad (self):
        return self._edad
    
    def setEdad (self, ed):
        self._edad = ed
        
    def getHabitat (self):
        return self._habitat
    
    def setHabitat (self, hab):
        self._habitat = hab
    
    def getGenero (self):
        return self._genero
    
    def setGenero (self, gen):
        self._genero = gen
        
    def getZona (self):
        return self._zona
    
    def setZona (self, zon):
        self._zona = zon
    
    def movimiento(self):
        return
       
    def totalPorTipo(self):
        totalTipo = "Mamiferos: " + str(Mamifero.cantidadMamiferos()) + "\n" + "Aves: " + str(Ave.cantidadAves()) + "\n" + "Reptiles: " + str(Reptil.cantidadReptiles()) + "\n" + "Peces: " + str(Pez.cantidadPeces()) + "\n" + "Anfibios: " + str(Anfibio.cantidadAnfibios())
        return totalTipo
    
    def toString(self):
        if self._zona == None:
            formato = "Mi nombre es " + str(self.getNombre()) + ", tengo una edad de " + str(self.getEdad()) + ", habito en " + str(self.getHabitat()) + " y mi genero es " + str(self.getGenero()) +  "."
        
        if self._zona != None:
            formato = "Mi nombre es " + str(self.getNombre()) + ", tengo una edad de " + str(self.getEdad()) + ", habito en " + str(self.getHabitat()) + " y mi genero es " + str(self.getGenero()) +  ", la zona en la que me ubico es " + str(self.getZona()) + ", en el " + str(self.getZona().getZoo())   
        return formato