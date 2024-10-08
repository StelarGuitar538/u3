from nodo import Nodo

class Pila:
    def __init__(self):
        self.__tope = None #inicializar la pila como vacia
        self.__cant = 0 #contador de elementos en la pila
        
    def vacia(self):
        return self.__tope == None
    
    def insertar(self, x):
        nuevo = Nodo(x) #crear un nuevo nodo
        nuevo.cargarSig(self.__tope) #el siguiente del nuevo nodo es el ultimo del pila
        self.__tope = nuevo #el ultimo del pila es el tope
        self.__cant += 1
        
    def suprimir(self):
        if self.vacia():
            print("pila vacia")
            return 0
        valor = self.__tope.obtenerDato() #obtener el valor del ultimo elemento
        self.__tope = self.__tope.obtenerSig() #el siguiente del ultimo elemento es el tope
        self.__cant -= 1
        return valor
    
   
    def mostrar(self):
        if not self.vacia():
            actual = self.__tope
            while actual is not None:
                print(actual.obtenerDato(), end=" ")
                actual = actual.obtenerSig()
            print("")
            
if __name__ == "__main__":
    p = Pila()
    p.insertar(1)
    p.insertar(2)
    p.insertar(3)
    p.mostrar()
    p.suprimir()
    p.suprimir()
    p.mostrar()
    
        