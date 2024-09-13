from nodo import Nodo

class Cola:
    __cant: int
    __ult: Nodo
    __pr: Nodo
    
    def __init__(self):
        self.__cant = 0
        self.__ult = None
        self.__pr = None
        
    def vacia(self):
        return self.__cant == 0
    
    def insertar(self, x):
        nuevo = Nodo(x)
        if self.vacia():
            nuevo.setSiguiente(None)
            self.__ult = None
            self.__pr = None
        else:
            self.__ult.setSiguiente(nuevo)
            self.__ult = nuevo
        self.__cant +=1
        
    def suprimir(self):
        if not self.vacia():
            x = self.__pr.getDato()
            self.__pr = self.__pr.getSiguiente()
            self.__cant -=1
            return x
        
    def mostrar(self):
        actual = self.__pr
        if not self.vacia():
            while actual is not None:
                print(actual.getDato(), end=' ')
                actual = actual.getSiguiente()
            print()
            