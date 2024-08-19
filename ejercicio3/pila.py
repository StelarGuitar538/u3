from nodo import Nodo

class Pila:
    def __init__(self):
        self.cabeza = None
        
    def vacia(self):
        return self.cabeza == None
    
    def insertar(self, dato):
        nuevo = Nodo(dato)
        nuevo.setSiguiente(self.cabeza)
        self.cabeza = nuevo
        
    def eliminar(self):
        if self.vacia():
            raise Exception("La pila esta vacia")
        else:
            dato = self.cabeza.getDato()
            self.cabeza = self.cabeza.getSiguiente()
            return dato
        
