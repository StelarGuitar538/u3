from nodo import Nodo
class listaEncadenada:
    __cabeza:Nodo
    __cont:int

    def _init_(self):
        self.__cabeza=None
        self.__cont=0

    def vacia(self):
        return self.__cont==0
    
    def primerElemento(self):
        return self.__cabeza.getDato()
    def ultimoElemento(self):
        aux=self.__cabeza
        while aux != None:
            retorna=aux.getDato()
            aux=aux.getSiguiente()
        return retorna
    
    def anterior(self,pos):
        elemento=None   
        if pos>=0 and pos<self.__cont:
            if pos==0:
                print("El indice ingresado no cuenta con anterior; es el primero")
            else:
                i=0
                aux=self.__cabeza
                while i<pos-1:
                    aux=aux.getSiguiente()
                    i+=1
                elemento=aux.getDato()
        else:
            print("El indice ingresado no es valido")
        return elemento
    
    def siguiente(self,pos):
        elemento=None
        if pos>=0 and pos<self.__cont:
            if pos==self.__cont-1:
                print("El indice ingresado no cuenta con siguiente; es el ultimo")
            else:
                i=0
                aux=self.__cabeza
                while i<=pos:
                    aux=aux.getSiguiente()
                    i+=1
                elemento=aux.getDato()
        else:
            print("El indice ingresado no es valido")
        return elemento

    def insertar(self, dato, posicion):
        nuevoNodo=Nodo(dato)
        if posicion >= 0 and posicion <= self.__cont:            
        
            if posicion==0:
                nuevoNodo.setSiguiente(self.__cabeza)
                self.__cabeza=nuevoNodo
                self.__cont+=1  

            else:
                actual=self.__cabeza
                indice=0

                while actual != None and indice < posicion-1:
                    actual=actual.getSiguiente()
                    indice += 1

                if actual is None:
                    print("Indice fuera de rango")
                    return
                else:
                    nuevoNodo.setSiguiente(actual.getSiguiente())
                    actual.setSiguiente(nuevoNodo)
                    self.__cont+=1
        else:
            print("Indice fuera de rango")
            return

    def suprimir(self,posicion):
        if self.vacia():
            print("La lista se encuentra vacia")
        else:
            if posicion>=0 and posicion<self.__cont:
                actual=self.__cabeza
                elemento=None

                if posicion==0:
                    self.__cabeza=actual.getSiguiente()
                else:
                    anterior=actual
                    actual=actual.getSiguiente()
                    i=1
                    while i<posicion:
                        anterior=actual
                        actual=actual.getSiguiente()
                        i+=1
                    anterior.setSiguiente(actual.getSiguiente())
                self.__cont-=1
                elemento=actual.getDato()
            return elemento
        
    def buscar(self,dato):
        aux=self.__cabeza
        band=False
        pos=None
        i=0
        while aux is not None and band is False:
            if aux.getDato() == dato:
                band=True
                pos=i
            else:
                i+=1
                aux=aux.getSiguiente()
        if band is False:
            print(f"El elemento {dato} no se encuentra en la lista")
        return pos

    def recuperar(self,pos):
        aux=self.__cabeza
        i=0
        if pos>=0 and pos<self.__cont:
            while i!=pos:
                aux=aux.getSiguiente()
                i+=1
            elemento=aux.getDato()
        else:
            elemento=None
            print("El indice ingresado no es valido")
        return elemento

    def mostrar(self):
        actual=self.__cabeza
        esPrimero=True
        while actual is not None:
            if esPrimero==True:
                print(f"{actual.getDato()}", end="")
                esPrimero=False
            else:
                print(f", {actual.getDato()}", end="")
            actual=actual.getSiguiente()
        print("")
                

if __name__=="__main__":
    lista = listaEncadenada()
    print("prueba")
    lista.insertar(10,0)
    lista.insertar(5,1)
    lista.insertar(15,2)
    lista.insertar(7,3)
    print("\nLista de elementos: ")
    lista.mostrar()
    print("Desplazamientos")
    lista.insertar(15,0)
    lista.insertar(7,1)
    lista.mostrar()
    print(f"El primer elemento es: {lista.primerElemento()}")
    print(f"El ultimo elemento es: {lista.ultimoElemento()}")
    print(f"Se elimina el {lista.suprimir(0)}")
    lista.mostrar()
    print(f"El elemento 10 está en la posicion {lista.buscar(10)}")
    print(f"En la posición 2 se encuentra el elemento {lista.recuperar(2)}")
    print(f"El elemento siguiente a la posicion 2 es el {lista.siguiente(2)}")
    print(f"El elemento anterior a la posicion 1 es el {lista.anterior(1)}")