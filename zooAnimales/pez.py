from zooAnimales.animal import Animal

class Pez(Animal):
    _Peces = []
    salmones = 0
    bacalaos = 0
    numPeces = 0
    def __init__(self, nombre, edad, habitat, genero, colorEscamas, cantidadAletas, zona = None, totalAnimales = 0):
        super().__init__(nombre, edad, habitat, genero, zona, totalAnimales)
        self._colorEscamas = colorEscamas
        self._cantidadAletas = cantidadAletas
          
    def getColorEscamas(self):
        return self._colorEscamas
    
    def setColorEscamas(self, col):
        self._colorEscamas = col
    
    def getCantidadAletas(self):
        return self._cantidadAletas
    
    def setCantidadAletas(self, cantal):
        self._cantidadAletas = cantal
    
    @classmethod
    def getPeces(cls):
        return cls._Peces
    
    @classmethod
    def setPeces(cls, list):
        cls._Peces.append(list)
    
    @classmethod
    def cantidadPeces(cls):
        cls.numPeces = cls.salmones + cls.bacalaos
        return cls.numPeces

    @classmethod
    def Salmones(cls):
        cls.salmones += 1
    
    @classmethod
    def Bacalaos(cls):
        cls.bacalaos += 1
    
    def movimiento():
        return
    
    @classmethod
    def crearSalmon(cls, nombre, edad, genero):
        cls.Salmones()
        cls.setPeces(Pez(nombre, edad, "oceano", genero, "rojo", 6))
    
    @classmethod
    def crearBacalao(cls, nombre, edad, genero):
        cls.Bacalaos()
        cls.setPeces(Pez(nombre, edad, "oceano", genero, "gris", 6)) 