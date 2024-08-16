class Nodo:
    def __init__(self, dato = None):
        self.__dato = dato
        self.__siguiente = None
        
    def obtenerDato(self):
        return self.__dato
    
    def obtenerSig(self):
        return self.__siguiente
    
    def cargarSig(self, sig):
        self.__siguiente = sig