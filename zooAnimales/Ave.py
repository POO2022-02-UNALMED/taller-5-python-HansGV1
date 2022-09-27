from gestion import Zoologico
from zooAnimales import Mamifero
from zooAnimales import Ave
from zooAnimales import Pez
from zooAnimales import Reptil
from zooAnimales import Anfibio

class Ave:
    def __init__(self, ave, aguilas, halcones, colorPlumas, numAves):
        self.ave = ave
        self.aguilas = aguilas
        self.halcones = halcones
        self.colorPlumas = colorPlumas
        self.numAves = numAves
    
    def Ave(self, nombre, edad, habitat,  genero, color): 
        self.colorPlumas= color
        Zoologico.setNombre(nombre)
        Zoologico.setEdad(edad)
        Zoologico.setHabitat(habitat)
        Zoologico.setGenero(genero)
    
    def Ave(self): 
        self.numAves += 1	
    
    def movimiento():
        return "volar"
    
    def crearHalcon(self, nombre, edad,  genero): 
        self.ave.add(Ave(nombre,edad,"montana",genero,"cafe glorioso"))
        self.numAves += 1		
        self.halcones+=	1
        return self.ave.get(self.ave.size()-1)
    
    def crearAguila(self, nombre, edad,  genero): 
        self.ave.add(Ave(nombre,edad,"montana",genero,"blanco y amarillo"))
        self.numAves += 1		
        self.aguilas += 1
        return self.ave.get(self.ave.size()-1)
    
    def cantidadAves(self):
        return self.numAves	
    
    def getColorPlumas(self): 
        return self.colorPlumas
		
