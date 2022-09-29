from zooAnimales.animal import Animal

class Pez(Animal):
    def __init__(self, totalAnimales, nombre, edad, habitat, genero, zona, listado, salmones, bacalaos, colorEscamas, cantidadAletas):
        super().__init__(totalAnimales, nombre, edad, habitat, genero, zona)
        self._listado = listado
        self.salmones = salmones
        self.bacalaos = bacalaos
        self._colorEscamas = colorEscamas
        self._cantidadAletas = cantidadAletas
        
    def getListado(self):
        return self._listado
    
    def setListado(self, list):
        self._listado = list
    
    def getColorEscamas(self):
        return self._colorEscamas
    
    def setColorEscamas(self, col):
        self._colorEscamas = col
    
    def getCantidadAletas(self):
        return self._cantidadAletas
    
    def setCantidadAletas(self, cantal):
        self._cantidadAletas = cantal
    
    def cantidadReptiles(self):
        peces = self.salmones + self.bacalaos
        return peces
    
    def movimiento():
        return
    
    def crearSalmon(self, sali, **kwargs):
        self.salmones += 1
        sali = Pez(colorEscamas = "rojo", cantidadAletas = "6", habitat = "oceano", **kwargs)
        return sali
    
    def crearBacalao(self, baca, **kwargs):
        self.bacalaos += 1
        baca = Pez(colorEscamas = "gris", cantidadAletas = "6", habitat = "oceano", **kwargs)  
        return baca