class Nodo:
    def __init__(self, dato = None):
        self.__sig = None
        self.__dato = dato
        
    def getSiguiente(self):
        return self.__sig
    
    def setSiguiente(self, sigu):
        self.__sig = sigu
    
    def getDato(self):
        return self.__dato