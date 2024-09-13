from nodo import Nodo

class Pila:
    def __init__(self):
        self.__tope = None
        self.__cant = 0
        
    def vacia(self):
        return self.__tope == None
    
    def insertar(self, x):
        nuevo = Nodo(x)
        nuevo.cargarSig(self.__tope)
        self.__tope = nuevo
        self.__cant += 1
        
    def suprimir(self):
        x = self.__tope.obtenerDato()
        self.__tope = self.__tope.obtenerSig()
        self.__cant -= 1
        return x
    
    def mostrar(self):
        if not self.vacia():
            actual = self.__tope
            while actual is not None:
                print(actual.obtenerDato(), end=" ")
                actual = actual.obtenerSig()
            print("")

if __name__ == "__main__":
    p = Pila()
    p.insertar(1)
    p.insertar(2)
    p.insertar(3)
    p.mostrar()
    p.suprimir()
    p.suprimir()
    p.mostrar()
    