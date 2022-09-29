from zooAnimales.animal import Animal

class Reptil(Animal):
    _Reptiles = []
    numReptiles = 0
    iguanas = 0
    serpientes = 0
    def __init__(self, nombre, edad, habitat, genero, colorEscamas, largoCola, zona = None, totalAnimales = 0):
        super().__init__(nombre, edad, habitat, genero, zona, totalAnimales)
        self._colorEscamas = colorEscamas
        self._largoCola = largoCola
        
    def getColorEscamas(self):
        return self._colorEscamas
    
    def setColorEscamas(self, col):
        self._colorEscamas = col
    
    def getLargoCola(self):
        return self._largoCola
    
    def setLargoCola(self, lar):
        self._largoCola = lar
    
    @classmethod
    def getReptiles(cls):
        return cls._Reptiles
    
    @classmethod
    def setReptiles(cls, list):
        cls._Reptiles.append(list)
    
    @classmethod
    def cantidadReptiles(cls):
        cls.numReptiles = cls.iguanas + cls.serpientes
        return cls.numReptiles
    
    def movimiento():
        return
    
    @classmethod
    def Iguanas(cls):
        cls.iguanas += 1
    
    @classmethod
    def Serpientes(cls):
        cls.serpientes += 1
    
    @classmethod
    def crearIguana(cls, nombre, edad, genero):
        cls.Iguanas()
        cls.setReptiles(Reptil(nombre, edad, "humedal", genero, "verde", 3))
       
    @classmethod
    def crearSerpiente(cls, nombre, edad, genero):
        cls.Serpientes()
        cls.setReptiles(Reptil(nombre, edad, "jungla", genero, "blanco", 1, ))