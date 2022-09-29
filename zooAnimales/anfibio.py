from zooAnimales import animal

class Anfibio(animal.Animal):
    def __init__(self, nombre, edad, habitat, genero, colorPiel, venenoso, zona = None, totalAnimales = 0, listado = None, ranas = None, salamandras = None):
        super().__init__(nombre, edad, habitat, genero, zona, totalAnimales)
        self._listado = listado
        self.ranas = ranas
        self.salamandras = salamandras
        self._colorPiel = colorPiel
        self._venenoso = venenoso
    
    def getListado (self):
        return self._listado
    
    def setListado (self, lis):
        self._listado = lis
    
    def getColorPiel (self):
        return self._colorPiel
    
    def setColorPiel (self, colp):
        self._colorPiel = colp
        
    def isVenenoso (self):
        return self._venenoso
    
    def setVenenoso (self, poi):
        self._venenoso = poi
    
    def cantidadAnfibios(self):
        anfibios = self.ranas + self.salamandras
        return anfibios
    
    def movimiento():
        return
    
    def crearRana(self, frog, **kwargs):
        self.ranas += 1
        frog = Anfibio(colorPiel = "rojo", venenoso = True, habitat = "selva", **kwargs)
        return frog
    
    def crearSalamandra(self, baca, **kwargs):
        self.salamandras += 1
        baca = Anfibio(colorPiel = "negro y amarillo", venenoso = False, habitat = "selva", **kwargs)  
        return baca