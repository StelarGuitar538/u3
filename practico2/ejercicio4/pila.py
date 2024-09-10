from nodo import Nodo

class Pila:
    def __init__(self):
        self.__cabeza = None
        
    def vacia(self):
        return self.__cabeza == None
    
    def insertar(self, dato):
        nuevo = Nodo(dato)
        nuevo.setSiguiente(self.__cabeza)
        self.__cabeza = nuevo
        
    def eliminar(self):
        if self.vacia():
            raise Exception("La pila esta vacia")
        else:
            dato = self.__cabeza.getDato()
            self.__cabeza = self.__cabeza.getSiguiente()
            return dato
        
    def mostrarContenido(self):
        actual = self.__cabeza
        c = 0
        while actual != None:
            c += 1
            actual = actual.getSiguiente()
        return c
    
    def verTope(self):
        if self.vacia():
            raise Exception("La pila está vacía")
        return self.__cabeza.getDato()  # Devuelve el dato del nodo en la cima