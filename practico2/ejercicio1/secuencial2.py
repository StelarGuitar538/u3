import numpy as np

class Secuencial:
    def __init__(self, max):
        self.__cant = max
        self.__ult = -1
        self.__items = np.zeros(self.__cant, dtype=int)
        
    def vacia(self):
        return self.__ult == -1
    
    def insertar(self, x):
        if self.__ult < self.__cant -1:
            self.__ult +=1
            self.__items[self.__ult] = x
            
            
    def suprimir(self):
        if not self.vacia():
            x = self.__items[self.__ult]
            self.__ult -=1
            return x
    
    def mostrar(self):
         if not self.vacia():
            for i in range(self.__ult, -1, -1):
                print(self.__items[i])
        
if __name__ == "__main__":
    c = Secuencial(3)
    c.insertar(65)
    c.insertar(2)
    c.mostrar()
    c.suprimir()
    c.mostrar()
    