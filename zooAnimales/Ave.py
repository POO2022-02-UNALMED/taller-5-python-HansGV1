from gestion import zoologico
from zooAnimales import mamifero
from zooAnimales import ave
from zooAnimales import pez
from zooAnimales import reptil
from zooAnimales import anfibio

class Ave:
    def __init__(self, ave, aguilas, halcones, colorPlumas, numaves):
        self.ave = ave
        self.aguilas = aguilas
        self.halcones = halcones
        self.colorPlumas = colorPlumas
        self.numaves = numaves
    
    def ave(self, nombre, edad, habitat,  genero, color): 
        self.colorPlumas= color
        zoologico.setNombre(nombre)
        zoologico.setEdad(edad)
        zoologico.setHabitat(habitat)
        zoologico.setGenero(genero)
    
    def ave(self): 
        self.numaves += 1	
    
    def movimiento():
        return "volar"
    
    def crearHalcon(self, nombre, edad,  genero): 
        self.ave.add(ave(nombre,edad,"montana",genero,"cafe glorioso"))
        self.numaves += 1		
        self.halcones+=	1
        return self.ave.get(self.ave.size()-1)
    
    def crearAguila(self, nombre, edad,  genero): 
        self.ave.add(ave(nombre,edad,"montana",genero,"blanco y amarillo"))
        self.numaves += 1		
        self.aguilas += 1
        return self.ave.get(self.ave.size()-1)
    
    def cantidadaves(self):
        return self.numaves	
    
    def getColorPlumas(self): 
        return self.colorPlumas
		
