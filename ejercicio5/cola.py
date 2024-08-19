from nodo import Nodo

class Cola:
    __cant: int
    __pr: Nodo
    __ult: Nodo
    
    def __init__(self):
        self.__cant = 0
        self.__pr = None
        self.__ult = None
        
    def vacia(self):
        return self.__cant == 0
    
    def insertar(self, x):
        nuevo = Nodo(x)
        if self.vacia():
            nuevo.setSiguiente(None)
            self.__pr = nuevo
            self.__ult = nuevo
        else:
            self.__ult.setSiguiente(nuevo)
            self.__ult = nuevo
            self.__ult.setSiguiente(None)
        self.__cant += 1
        
    def suprimir(self):
        if self.vacia():
            print("cola vacia")
            return 0
        else:
            x = self.__pr.getDato()
            self.__pr = self.__pr.getSiguiente()
            self.__cant -= 1
            return x
        
    def mostrar(self, primero):
        if primero != None:
            print(primero.getDato())
            self.mostrar(primero.getSiguiente())
