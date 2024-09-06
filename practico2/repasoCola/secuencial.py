import numpy as np

class colaSecuencial:
    def __init__(self, max=5):
        self.__cant = 0
        self.__pr = 0
        self.__ult = 0
        self.__max = max
        self.__items = np.empty(self.__max, dtype=object)
        
    def insertar(self, x):
        if self.__cant < self.__max:
            self.__items[self.__ult] = x
            self.__ult = (self.__ult +1) % self.__max
            self.__cant +=1
            return x
        
    def suprimir(self):
        if not self.vacia():
            x = self.__items[self.__pr]
            self.__pr = int((self.__pr+1) %self.__max)
            self.__cant -=1
            return x
    
    def mostrar(self):
        if not self.vacia():
            for i in range(self.__cant):
                print(self.__items[i])
     