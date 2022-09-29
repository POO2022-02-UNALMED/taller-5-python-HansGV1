class Zoologico:
    _zonas = []
    numTotalAnimales = 0
    def __init__(self, nombre, ubicacion):
        self._nombre = nombre
        self._ubicacion = ubicacion
    
    def getNombre (self):
        return self._nombre
    
    def setNombre (self, nom):
        self._nombre = nom
        
    def getUbicacion (self):
        return self._ubicacion
    
    def setUbicacion (self, ubi):
        self._ubicacion = ubi
    
    @classmethod 
    def getZona (cls):
        return cls._zonas

    @classmethod
    def agregarZonas(cls, zon):
        cls._zonas.append(zon)
    
    @classmethod
    def cantidadTotalAnimales(cls):
        a = cls.getZonas()
        for i in a:
            cls.numTotalAnimales += i.cantidadAnimales()
        return cls.numTotalAnimales