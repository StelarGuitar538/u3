import numpy as np

class ListaSecuencial:
    def __init__(self, tamanio = 5):
        self.__tamanio = tamanio
        self.__ultimo = -1
        self.__cantidad = 0
        self.__arreglo = np.empty(self.__tamanio, dtype=int)
        
    def vacia(self):
        return self.__cantidad == 0
    
    def lleno(self):
        return self.__cantidad == self.__tamanio
    
    def insertar(self, dato, posicion):
        if not self.lleno():
            if posicion >=0 and posicion <= self.__ultimo+1:
                i = self.__ultimo + 1
                while i > posicion:
                    self.__arreglo[i] = self.__arreglo[i-1]
                    i -= 1
                    self.__arreglo[i] = dato
                    self.__ultimo += 1
                    self.__cantidad += 1
            else:
                print("Posición fuera de rango")
        else:
            print("Lista llena")
    
    def insertarPorContenido(self, dato):
        if not self.lleno():
            if self.vacia():
                self.__ultimo += 1
                self.__arreglo[self.__ultimo] = dato
                self.__cantidad += 1
                print(f"Elemento insertado: {dato}")
            else:
                i=0
                while i <= self.__ultimo and self.__arreglo[i] < dato:
                    i += 1
                for j in range(self.__ultimo+1, i-1, -1):
                    self.__arreglo[j] = self.__arreglo[j-1]
                self.__arreglo[i] = dato
                self.__ultimo += 1
                self.__cantidad += 1
                print(f"Elemento insertado: {dato}")
        else:
            print("Lista llena")
            
    def recorrer(self):
        i=0
        if not self.vacia():
            while i <= self.__ultimo:
                print(self.__arreglo[i])
                i += 1
                
    def suprimir(self, pos):
        if not self.vacia():
            if pos >= 0 and pos <= self.__ultimo:
                i = self.__ultimo
                eliminado = self.__arreglo[pos]
                while i > pos:
                    self.__arreglo[pos] = self.__arreglo[pos+1]
                    pos += 1
                self.__cantidad -= 1
                self.__ultimo -= 1
                print(f"Elemento eliminado: {eliminado}")
            else:
                print("Posición fuera de rango")
        else:
            print("Lista vacia")
    
    def suprimirPorContenido(self, dato):
        if not self.vacia():
            i = 0
            while i <= self.__ultimo and self.__arreglo[i] != dato:
                i += 1
                if i <= self.__ultimo:
                    for j in range(i, self.__ultimo):
                        self.__arreglo[j] = self.__arreglo[j+1]
                    self.__ultimo -= 1
                    self.__cantidad -= 1
                    print(f"Elemento eliminado: {dato}")
        else:
            print("Lista vacia")
            
    def buscar(self, dato):
        if not self.vacia():
            i = 0
            while i <= self.__ultimo and self.__arreglo[i] != dato:
                i += 1
                if i <= self.__ultimo:
                    print(f"Elemento encontrado: {dato} en posicion {i}")
        else:
            print("Lista vacia")
            
    def primerElemento(self):
        if not self.vacia():
            return self.__arreglo[0]
        
    def ultimoElemento(self):
        if not self.vacia():
            return self.__arreglo[self.__ultimo]
        
    def siguiente(self, pos):
        if not self.vacia():
            if pos == self.__ultimo:
                print("No hay mas elementos")
            else:
                if pos >= 0 and pos <= self.__ultimo:
                    print(f"el elemento siguiente es {self.__arreglo[pos+1]}")
                    
    def anterior(self, pos):
        if not self.vacia():
            if pos == 0:
                print("No hay mas elementos")
            else:
                if pos >= 0 and pos <= self.__ultimo:
                    print(f"el elemento anterior es {self.__arreglo[pos-1]}")

if __name__ == "__main__":
    lista = ListaSecuencial(5)
    lista.insertarPorContenido(10)
    lista.insertarPorContenido(20)
    lista.insertarPorContenido(30)
    lista.insertarPorContenido(40)
    lista.recorrer()
    lista.suprimirPorContenido(40)
    lista.recorrer()
    lista.insertar(1, 0)
    lista.insertar(2, 1)
    lista.insertar(3, 0)
    lista.recorrer()
    lista.suprimir(0)
    lista.buscar(3)
    
    lista.primerElemento()
    lista.ultimoElemento()
    lista.siguiente(0)
    lista.anterior(1)