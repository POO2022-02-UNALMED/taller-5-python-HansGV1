import zooAnimales

class Animal:
    _zona = []
    _totalAnimales = 0
    def __init__(self, nombre, edad, habitat, genero):
        self._nombre = nombre
        self._edad = edad
        self._habitat = habitat
        self._genero = genero
  
    def getNombre (self):
        return self._nombre
    
    def setNombre (self, nom):
        self._nombre = nom
        
    def getEdad (self):
        return self._edad
    
    def setEdad (self, ed):
        self._edad = ed
        
    def getHabitat (self):
        return self._habitat
    
    def setHabitat (self, hab):
        self._habitat = hab
    
    def getGenero (self):
        return self._genero
    
    def setGenero (self, gen):
        self._genero = gen

    @classmethod
    def getTotalAnimales (cls):
        return cls._totalAnimales
    
    @classmethod
    def setAnimales(cls):
        cls._totalAnimales = zooAnimales.mamifero.Mamifero.cantidadMamiferos() + zooAnimales.ave.Ave.cantidadAves() + zooAnimales.reptil.Reptil.cantidadReptiles() + zooAnimales.pez.Pez.cantidadPeces() + zooAnimales.anfibio.Anfibio.cantidadAnfibios()
    
    @classmethod 
    def getZona (cls):
        return cls._zona
    
    @classmethod
    def setZona (cls, zon):
        cls._zona = zon
    
    def movimiento(self):
        return
       
    def totalPorTipo():
        totalTipo = "Mamiferos : " + str(zooAnimales.mamifero.Mamifero.cantidadMamiferos()) + "\nAves : " + str(zooAnimales.ave.Ave.cantidadAves()) + "\nReptiles : " + str(zooAnimales.reptil.Reptil.cantidadReptiles()) + "\nPeces : " + str(zooAnimales.pez.Pez.cantidadPeces()) + "\nAnfibios : " + str(zooAnimales.anfibio.Anfibio.cantidadAnfibios())
        return totalTipo
    
    def toString(self):
        if self._zona == []:
            formato = "Mi nombre es " + str(self.getNombre()) + ", tengo una edad de " + str(self.getEdad()) + ", habito en " + str(self.getHabitat()) + " y mi genero es " + str(self.getGenero()) +  "."
        
        if self._zona != []:
            formato = "Mi nombre es " + str(self.getNombre()) + ", tengo una edad de " + str(self.getEdad()) + ", habito en " + str(self.getHabitat()) + " y mi genero es " + str(self.getGenero()) +  ", la zona en la que me ubico es " + str(self.getZona()) + ", en el " + str(self.getZona().getZoo())   
        return formato