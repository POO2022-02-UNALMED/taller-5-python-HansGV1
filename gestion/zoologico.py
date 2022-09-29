class Zoologico:
    _zonas = []
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
    def getZonas (cls):
        return cls._zonas
    
    @classmethod
    def agregarZonas(cls, zon):
        cls._zonas.append(zon)
    
    def cantidadTotalAnimales(self):
        a = self.getZonas()
        cantidad = 0
        for i in a:
            cantidad += i.cantidadAnimales()
        return cantidad