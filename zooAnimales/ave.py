from zooAnimales.animal import Animal

class Ave(Animal):
    def __init__(self, totalAnimales, nombre, edad, habitat, genero, zona, listado, halcones, aguilas, colorPlumas):
        super().__init__(totalAnimales, nombre, edad, habitat, genero, zona)
        self._listado = listado
        self.halcones = halcones
        self.aguilas = aguilas
        self._colorPlumas = colorPlumas
        
    def getListado(self):
        return self._listado
    
    def setListado(self, list):
        self._listado = list
    
    def getColorPlumas(self):
        return self._colorPlumas
    
    def setColorPlumas(self, col):
        self._colorPlumas = col
    
    def cantidadAves(self):
        aves = self.halcones + self.aguilas
        return aves
    
    def movimiento():
        return
    
    def crearHalcon(self, falcon, **kwargs):
        self.halcones += 1
        falcon = Ave(colorPlumas = "cafe glorioso", habitat = "montanas", **kwargs)        
        return falcon
    
    def crearAguilas(self, eagle, **kwargs):
        self.aguilas += 1
        eagle = Ave(colorPlumas = "blanco y amarillo", habitat = "montanas", **kwargs)        
        return eagle