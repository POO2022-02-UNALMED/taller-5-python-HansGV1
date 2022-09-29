from gestion.zoologico import Zoologico
from zooAnimales.animal import Animal

class Zona:
    def __init__(self, nombre, zoo = None, animales = [], aa = {}, numAnimales = 0):
        self._nombre = nombre
        self._zoo = zoo
        self._animales = animales
        self.aa = aa
        self.numAnimales = numAnimales

    def getZona():
        return Animal.getZona()

    def getNombre (self):
        return self._nombre
    
    def setNombre (self, nom):
        self._nombre = nom
    
    def getZoo (self):
        return self._zoo
    
    def setZoo (self, zuu):
        self._zoo = zuu
    
    def getAnimales (self):
        return self._animales

    def agregarAnimales (self, ani):
        a = self.getNombre()
        if self._animales == []:
            self._animales.append([])
            self.aa[a] = 0
            self._animales[self.aa[a]].append(ani)
        
        elif self._animales != []:
            if a in self.aa:
                self._animales[self.aa[a]].append(ani)
            
            if not a in self.aa:
                self.aa[a] = len(self._animales)
                self._animales.append([])
                self._animales[self.aa[a]].append(ani)
        
    def cantidadAnimales(self):
        self.numAnimales += len(self.getAnimales()[self.aa[self.getNombre()]])
        return self.numAnimales