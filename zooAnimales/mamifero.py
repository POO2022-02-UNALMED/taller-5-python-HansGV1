from zooAnimales.animal import Animal

class Mamifero(Animal):
    def __init__(self, nombre, edad, habitat, genero, zona, listado, caballos, leones, pelaje, patas):
        super().__init__(nombre, edad, habitat, genero, zona)
        self._listado = listado
        self.caballos = caballos
        self.leones = leones
        self._pelaje = pelaje
        self._patas = patas
        
    def getListado(self):
        return self._listado
    
    def setListado(self, list):
        self._listado = list
    
    def getPelaje(self):
        return self._pelaje
    
    def setPelaje(self, col):
        self._pelaje = col
    
    def getPatas(self):
        return self._patas
    
    def setPatas(self, pat):
        self._patas = pat
    
    def cantidadMamiferos(self):
        mamiferos = self.caballos + self.leones
        return mamiferos

    def crearCaballo(self, horse, **kwargs):
        self.caballos += 1
        horse = Mamifero(pelaje = True, patas = 4, habitat = "pradera", **kwargs)        
        return horse
    
    def crearLeon(self, lion, **kwargs):
        self.leones += 1
        lion = Mamifero(pelaje = True, patas = 4, habitat = "selva", **kwargs)        
        return lion