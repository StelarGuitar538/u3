from pila import Pila


def moverDiscos(origen, destino):
    if origen.vacia():
        print("La pila esta vacia")
        return False
    if not destino.vacia() and origen.verTope() > destino.verTope():
        print("No se puede mover el disco")
        return False
    disco = origen.eliminar()
    destino.insertar(disco)
    return True
    
def main(n):
    p1 = Pila()
    p2 = Pila()
    p3 = Pila()
    
    for i in range(n, 0, -1):
        p1.insertar(i)

    jugadas = 0
    minJugadas = (n**2)-1
    
    while p3.mostrarContenido() != n:
        origen = int(input("ingrese pila origen: "))
        destino = int(input("ingrese pila destino: "))
        if origen == 1:
            origen = p1
        elif origen == 2:
            origen = p2
        elif origen == 3:
            origen = p3
            
        if destino == 1:
            destino = p1
        elif destino == 2:
            destino = p2
        elif destino == 3:
            destino = p3
            
        if moverDiscos(origen, destino):
            jugadas += 1
        
    print(f"El numero de jugadas minimo es {minJugadas} y el numero de jugadas que hizo fue {jugadas}")
    
if __name__ == "__main__": 
    n= int(input("ingrese cantidad de discos: "))
    main(n)
    