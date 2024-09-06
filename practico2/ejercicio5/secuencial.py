import numpy as np

class colaSecuencial:
    __cant: int
    __pr: int
    __ult: int
    __max: int
    __items: object
    
    def __init__(self, max=5):
        self.__cant=0
        self.__pr=0
        self.__ult=0
        self.__max=max
        self.__items = np.empty(self.__max, dtype=object)
        
    def vacia(self):
        return self.__cant == 0
    
    def insertar(self, x):
        if self.__cant < self.__max:
            self.__items[self.__ult] = x
            self.__ult = (self.__ult + 1) % self.__max
            self.__cant += 1
            return(x)
        else:
            return(0)
        
    def suprimir(self):
        if self.vacia():
            print("cola vacia")
        else:
            x = self.__items[self.__pr]
            self.__pr = int((self.__pr + 1) % self.__max)
            self.__cant -= 1
            return x
        
    def mostrar(self):
        if self.vacia():
            print("cola vacia")
        else:
            for i in range(self.__cant):
                print(self.__items[i])

if __name__ == "__main__":
    cola = colaSecuencial(5)
    cola.insertar(10)
    cola.insertar(20)
    cola.mostrar()
    print(cola.suprimir())
    cola.mostrar()