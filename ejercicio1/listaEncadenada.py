from ejercicio4.nodo import Nodo

class Lista:
    def __init__(self):
        self.__cabeza = None
        
    def vacia(self):
        return self.__cabeza == None
    
    def insertarAlInicio(self, x):
        nuevo = Nodo(x)
        nuevo.cargarSig(self.__cabeza)
        self.__cabeza = nuevo
        
    def insertarAlFinal(self, x):
        nuevo = Nodo(x)
        if self.vacia():
            self.__cabeza = nuevo
        else:
            actual = self.__cabeza
            while actual.obtenerSig() != None:
                actual = actual.obtenerSig()
            actual.cargarSig(nuevo)
            
    def suprimirAlInicio(self):
        if self.vacia():
            print("lista vacia")
            return 0
        else:
            x = self.__cabeza.obtenerDato()
            self.__cabeza = self.__cabeza.obtenerSig()
            return x
        
    def suprimirAlFinal(self):
        if self.vacia():
            print("lista vacia")
            return 0
        elif self.__cabeza.obtenerSig() == None: #si hay un solo elemento
            x = self.__cabeza.obtenerDato()
            self.__cabeza = None
            return x
        else:
            actual = self.__cabeza
            while actual.obtenerSig() != None:
                actual = actual.obtenerSig()
            x = actual.obtenerDato()
            actual.cargarSig(None)
            return x
        
    def mostrar(self):
        if self.vacia():
            print("lista vacia")
        else:
            actual = self.__cabeza
            while actual != None:
                print(actual.obtenerDato(), end = "->")
                actual = actual.obtenerSig()
                
                
    
            