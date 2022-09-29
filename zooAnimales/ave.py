from zooAnimales.animal import Animal

class Ave(Animal):
    _Aves = []
    halcones = 0
    aguilas = 0
    numAves = 0
    def __init__(self, nombre, edad, habitat, genero, colorPlumas, zona = None, totalAnimales = 0):
        super().__init__(nombre, edad, habitat, genero, zona, totalAnimales)
        self._colorPlumas = colorPlumas
        
    def getColorPlumas(self):
        return self._colorPlumas
    
    def setColorPlumas(self, col):
        self._colorPlumas = col
    
    @classmethod
    def getAves(cls):
        return cls._Aves
    
    @classmethod
    def setAves(cls, list):
        cls._Aves.append(list)
    
    @classmethod
    def cantidadAves(cls):
        cls.numAves = cls.halcones + cls.aguilas
        return cls.numAves
    
    def movimiento():
        return
    
    @classmethod
    def Halcones(cls):
        cls.halcones += 1
    
    @classmethod
    def Aguilas(cls):
        cls.aguilas += 1
    
    @classmethod
    def crearHalcon(cls, nombre, edad, genero):
        cls.Halcones()
        cls.setAves(Ave(nombre, edad, "montanas", genero, "cafe glorioso"))       
    
    @classmethod
    def crearAguila(cls, nombre, edad, genero):
        cls.Aguilas()
        cls.setAves(Ave(nombre, edad, "montanas", genero, "blanco y amarillo"))     