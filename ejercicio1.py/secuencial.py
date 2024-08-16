import numpy as np

class Pila:
    def __init__(self, xcant=0):
        self.__cant = xcant
        self.__tope = -1
        self.__items = np.zeros(self.__cant, dtype=int)  # inicializamos con numpy arrays
        
    def vacia(self):
        return self.__tope == -1
    
    def insertar(self, x):
        if self.__tope < self.__cant - 1:
            self.__tope += 1
            self.__items[self.__tope] = x
            return x
        else:
            return 0
        
    def suprimir(self):
        if self.vacia():
            print("Pila vacía")
            return 0
        else:
            x = self.__items[self.__tope]
            self.__tope -= 1
            return x
        
    def mostrar(self):
        if not self.vacia():
            for i in range(self.__tope, -1, -1):
                print(self.__items[i])