from ejercicio4.nodo import Nodo

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
    
   

            
    
        