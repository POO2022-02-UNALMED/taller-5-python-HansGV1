from zooAnimales.animal import Animal

class Reptil(Animal):
    def __init__(self, totalAnimales, nombre, edad, habitat, genero, zona, listado, iguanas, serpientes, colorEscamas, largoCola):
        super().__init__(totalAnimales, nombre, edad, habitat, genero, zona)
        self._listado = listado
        self.iguanas = iguanas
        self.serpientes = serpientes
        self._colorEscamas = colorEscamas
        self._largoCola = largoCola
        
    def getListado(self):
        return self._listado
    
    def setListado(self, list):
        self._listado = list
    
    def getColorEscamas(self):
        return self._colorEscamas
    
    def setColorEscamas(self, col):
        self._colorEscamas = col
    
    def getLargoCola(self):
        return self._largoCola
    
    def setLargoCola(self, lar):
        self._largoCola = lar
    
    def cantidadReptiles(self):
        reptiles = self.iguanas + self.serpientes
        return reptiles
    
    def movimiento():
        return
    
    def crearIguana(self, iguan, **kwargs):
        self.iguanas += 1
        iguan = Reptil(colorEscamas = "verde", largoCola = 3, habitat = "humedal", **kwargs)        
        return iguan
    
    def crearSerpiente(self, snake, **kwargs):
        self.serpientes += 1
        snake = Reptil(colorEscamas = "blanco", largoCola = 1, habitat = "jungla", **kwargs)       
        return snake