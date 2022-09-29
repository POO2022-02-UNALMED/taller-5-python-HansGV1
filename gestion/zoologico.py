class Zoologico:
    def __init__(self, nombre, ubicacion, zonas = None):
        self._nombre = nombre
        self._ubicacion = ubicacion
        self._zonas = zonas
    
    def getNombre (self):
        return self._nombre
    
    def setNombre (self, nom):
        self._nombre = nom
        
    def getUbicacion (self):
        return self._ubicacion
    
    def setUbicacion (self, ubi):
        self._ubicacion = ubi
        
    def getZonas (self):
        return self._zonas
    
    def agregarZonas(self, zon):
        self._zonas.append(zon)
    
    def cantidadTotalAnimales(self):
        a = self.getZonas()
        cantidad = 0
        for i in a:
            cantidad += i.cantidadAnimales()
        return cantidad