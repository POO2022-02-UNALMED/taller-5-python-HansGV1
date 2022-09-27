class Zoologico:
    def __init__(self, nombre, ubicacion, zonas):
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.zonas = zonas
        
    def Zoologico(self, nombre, ubicacion):
        self.nombre = nombre
        self.ubicacion = ubicacion
    
    def setNombre(self, nombre):
        self.nombre = nombre
    
    def getNombre(self):
        return self.nombre
    
    def setUbicacion(self, ubicacion):
        self.ubicacion = ubicacion
    
    def getUbicacion(self): 
        return self.ubicacion
    
    def setZona(self, zona):
        self.zonas.add(zona)
    
    def getZona(self):
        return self.zonas
    
    def agregarZonas(self, zona):
        self.zonas.add(zona)
        
    def cantidadTotalAnimales(self):
        numAnimal = 0
        for i in range(0, self.zonas.size()):
            numAnimal = numAnimal + self.zonas.get(i).cantidadAnimales()
            i += 1
        return numAnimal
