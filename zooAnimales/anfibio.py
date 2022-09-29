from zooAnimales.animal import Animal

class Anfibio(Animal):
    _anfibios = []
    ranas = 0
    salamandras = 0
    numAnfibios = 0
    def __init__(self, nombre, edad, habitat, genero, colorPiel, venenoso):
        super().__init__(nombre, edad, habitat, genero)
        self._colorPiel = colorPiel
        self._venenoso = venenoso
    
    def getColorPiel (self):
        return self._colorPiel
    
    def setColorPiel (self, colp):
        self._colorPiel = colp
        
    def isVenenoso (self):
        return self._venenoso
    
    def setVenenoso (self, poi):
        self._venenoso = poi
    
    @classmethod
    def getAnfibios (cls):
        return cls._anfibios
    
    @classmethod
    def setAnfibios (cls, lis):
        cls._anfibios.append(lis)
    
    @classmethod
    def cantidadAnfibios(cls):
        cls.numAnfibios = cls.ranas + cls.salamandras
        return cls.numAnfibios
          
    @classmethod
    def Anfibios(cls):
        cls.ranas += 1
    
    @classmethod
    def Salamandras(cls):
        cls.salamandras += 1
    
    def movimiento():
        return
    
    @classmethod
    def crearRana(cls, nombre, edad, genero):
        cls.Anfibios()
        cls.setAnfibios(Anfibio(nombre, edad, "selva", genero, "rojo", True))

    @classmethod
    def crearSalamandra(cls, nombre, edad, genero):
        cls.Salamandras()
        cls.setAnfibios(Anfibio(nombre, edad, "selva", genero, "negro y amarillo", False))