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
            nuevo.setSiguiente(nuevo)
            self.__ult = nuevo
            nuevo.setSiguiente(None)
            self.__cant +=1
            
    def suprimir(self):
        if not self.vacia():
            x = self.__pr.getDato()
            self.__pr = self.__pr.getSiguiente()
            self.__cant -=1
            return x