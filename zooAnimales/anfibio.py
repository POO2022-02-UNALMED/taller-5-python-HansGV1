from gestion import zoologico

class Anfibio(Animal):
    def __init__ (self, anfibio, ranas, salamandras, colorPiel, venenoso, numAnfi):
        self.anfibio = anfibio
        self.ranas = ranas
        self.salamandras = salamandras
        self.colorPiel = colorPiel
        self.venenoso = venenoso
        self.numAnfi = numAnfi
    
    def Anfibio(self, nombre, edad, habitat, genero, color, veneno):
        self.colorPiel = color
        self.venenoso=veneno
        zoologico.setNombre(nombre)
        zoologico.setEdad(edad)
        zoologico.setHabitat(habitat)
        zoologico.setGenero(genero)
        
    def Anfibio(self):
        self.numAnfi += 1
      
    def movimiento(self):
        return "saltar"
    
    def crearRana(self, nombre, edad, genero):
        self.anfibio.add(Anfibio(nombre, edad, "selva",genero,"rojo",True))
        self.ranas += 1
        self.numAnfi += 1
        return self.anfibio.get(self.anfibio.size()-1)
    
    def crearSalamandra(self, nombre, edad, genero):
        self.anfibio.add(Anfibio(nombre, edad, "selva",genero,"negro y amarillo",False))
        self.salamandras += 1
        self.numAnfi += 1
        return self.anfibio.get(self.anfibio.size()-1)
    
    def cantidadAnfibios(self):
        return self.numAnfi
    
    def isVenenoso(self):
        return self.venenoso
    
    def getColorPiel(self):
        return self.colorPiel
    
    def getNombre(self):
        return self.anfibio

