import numpy as np

class colaSecuencial:
    __cant: int
    __pr: int
    __ult: int
    __max: int
    __items: object
    
    def __init__(self, max=5):
        self.__cant = 0  # Cantidad de elementos en la cola
        self.__pr = 0  # Índice del primer elemento
        self.__ult = 0  # Índice del último elemento
        self.__max = max  # Capacidad máxima de la cola
        self.__items = np.empty(self.__max, dtype=object)  # Arreglo para almacenar los elementos de la cola
        
    def vacia(self):
        # Devuelve True si la cola está vacía, False en caso contrario
        return self.__cant == 0
    
    def insertar(self, x):
        # Inserta un elemento x al final de la cola
        if self.__cant < self.__max:
            self.__items[self.__ult] = x  # Agrega el elemento en la posición de __ult
            self.__ult = (self.__ult + 1) % self.__max  # Actualiza el índice __ult de forma circular
            self.__cant += 1  # Incrementa el contador de elementos
            return x
        else:
            print("Cola llena")
            return 0
        
    def suprimir(self):
        # Elimina el primer elemento de la cola
        if self.vacia():
            print("Cola vacía")
            return None
        else:
            x = self.__items[self.__pr]  # Guarda el elemento a eliminar
            self.__pr = (self.__pr + 1) % self.__max  # Actualiza el índice __pr de forma circular
            self.__cant -= 1  # Decrementa el contador de elementos
            return x
        
    def mostrar(self):
        # Muestra todos los elementos de la cola en el orden correcto
        if self.vacia():
            print("Cola vacía")
        else:
            i = self.__pr
            for _ in range(self.__cant):
                print(self.__items[i], end=' ')
                i = (i + 1) % self.__max  # Mueve de forma circular
            print()

if __name__ == "__main__":
    c = colaSecuencial()
    b = True

    while b:
        print("1. Insertar\n2. Suprimir\n3. Salir")
        op = int(input("Ingrese opción: "))

        if op == 1:
            elem = int(input("Ingrese elemento: "))
            c.insertar(elem)
            c.mostrar()
        elif op == 2:
            c.suprimir()
            c.mostrar()
        elif op == 3:
            b = False
        else:
            print("Opción no válida")
