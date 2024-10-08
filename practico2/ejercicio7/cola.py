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
        """Retorna True si la cola está vacía, de lo contrario False."""
        return self.__cant == 0
    
    def insertar(self, x):
        """Inserta un nuevo elemento en la cola."""
        nuevo = Nodo(x)
        if self.vacia():
            self.__pr = nuevo
            self.__ult = nuevo
        else:
            self.__ult.setSiguiente(nuevo)
            self.__ult = nuevo
        self.__cant += 1
        
    def suprimir(self):
        """Elimina el primer elemento de la cola y lo retorna. Si está vacía, devuelve 0."""
        if self.vacia():
            print("cola vacia")
            return 0
        else:
            x = self.__pr.getDato()
            self.__pr = self.__pr.getSiguiente()
            self.__cant -= 1
            if self.__pr is None:  # Si la cola queda vacía
                self.__ult = None
            return x
    
    def tamanio(self):
        """Devuelve el número de elementos en la cola."""
        return self.__cant
    
    def frente(self):
        """Devuelve el elemento que está en el frente de la cola sin eliminarlo."""
        if not self.vacia():
            return self.__pr.getDato()
        else:
            print("cola vacia")
            return None
