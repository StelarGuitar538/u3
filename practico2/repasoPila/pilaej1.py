from nodo import Nodo

class Pila:
    
    def __init__(self):
        self.__tope = None
        self.__cant = 0
        
    def vacia(self):
        return self.__tope == None
    
    def insertar(self, x):
        nuevo = Nodo(x)
        nuevo.setSiguiente(self.__tope)
        self.__tope = nuevo
        self.__cant +=1
        return x
        
    def suprimir(self):
        if not self.vacia():
            valor = self.__tope.getDato()
            self.__tope = self.__tope.getSiguiente()
            self.__cant -=1
            return valor