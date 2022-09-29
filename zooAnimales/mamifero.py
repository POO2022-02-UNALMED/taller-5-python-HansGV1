from zooAnimales.animal import Animal

class Mamifero(Animal):
    _mamiferos = []
    caballos = 0
    leones = 0
    numMamiferos = 0
    def __init__(self, nombre, edad, habitat, genero, pelaje , patas):
        super().__init__(nombre, edad, habitat, genero)
        self._pelaje = pelaje
        self._patas = patas
     
    def isPelaje(self):
        return self._pelaje
    
    def setPelaje(self, pel):
        self._pelaje = pel
    
    def getPatas(self):
        return self._patas
    
    def setPatas(self, pat):
        self._patas = pat
    
    @classmethod
    def getMamiferos(cls):
        return cls._mamiferos
    
    @classmethod
    def setMamiferos(cls, lis):
        cls._mamiferos.append(lis)
      
    @classmethod
    def cantidadMamiferos(cls):
        cls.numMamiferos = cls.caballos + cls.leones
        return cls.numMamiferos
    
    @classmethod
    def Caballos(cls):
        cls.caballos += 1
    
    @classmethod
    def Leones(cls):
        cls.leones += 1

    @classmethod
    def crearCaballo(cls, nombre, edad, genero):
        cls.Caballos()
        cls.setMamiferos(Mamifero(nombre, edad, "pradera", genero, True, 4))
    
    @classmethod
    def crearLeon(cls, nombre, edad, genero):
        cls.Leones()
        cls.setMamiferos(Mamifero(nombre, edad, "selva", genero, True, 4))  