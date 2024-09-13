import numpy as np

class Cola:
    def __init__(self, max):
        self.__max = max
        self.__ult = 0
        self.__pr = 0
        self.__cant = 0
        self.__items = np.empty(self.__max, dtype=int)
        
    def insertar(self, x):
        if self.__cant < self.__max:
            self.__items[self.__ult] = x
            self.__ult = (self.__ult + 1) % self.__max
            self.__cant +=1
            
    def suprimir(self):
        if not self.vacia():
            x = self.__items[self.__pr]
            self.__pr = (self.__pr +1) % self.__max
            self.__cant -=1
            return x