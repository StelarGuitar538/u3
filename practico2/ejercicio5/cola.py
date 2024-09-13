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
        
    def mostrar(self):
        actual = self.__pr
        if self.vacia():
            print("Cola vacía")
        else:
            while actual is not None:
                print(actual.getDato(), end=' ')
                actual = actual.getSiguiente()
            print()  # Para nueva línea después de imprimir todos los elementos

            
if __name__ == "__main__":
    c = Cola()
    c.insertar(1)
    c.insertar(2)
    c.insertar(3)
    c.mostrar()
    c.suprimir()
    c.suprimir()
    c.mostrar()
