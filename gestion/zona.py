class Zona:
    def __init__(self, nombre, zoo = None, animales = None):
        self._nombre = nombre
        self._zoo = zoo
        self._animales = animales

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

    def agregarAnimales(self, ani):
        self._animales.append(ani)
        
    def cantidadAnimales(self):
        cant = 0
        for i in self.getAnimales():
            cant += 1
        return cant