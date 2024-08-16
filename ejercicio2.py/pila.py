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
    
    def decimalABinario(self, x):
        if x == 0:
            return "0"
            
        entero = int(x)
            
        while entero > 0:
            residuo = entero % 2
            self.insertar(residuo)
            entero //= 2  # corregido para actualizar 'entero'
            
        binario = ""  # debe estar fuera del bucle anterior
        while not self.vacia():
            binario += str(self.suprimir())  # reconstruir el número binario
            
        return binario[::-1]  # devolver el binario en el orden correcto

            
    
        