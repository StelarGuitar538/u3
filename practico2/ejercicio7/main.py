from cola import Cola
import random 

def main():
    c1 = Cola()
    c2 = Cola()
    c3 = Cola()
    
    frecuencia1 = 5
    frecuencia2 = 3
    frecuencia3 = 4

    tac = 2
    tms = 120
    
    cajero1 =0
    cajero2 =0
    cajero3 =0
    reloj = 0
    acum = 0
    cant = 0
    sinAtender = 0
    lista = []
    
    def elegirCajero(c1, c2, c3, reloj):
        if c1.vacia() and c2.vacia() and c3.vacia():
            aleatorio = random.random()
            if aleatorio <= 0.33:
                return c1
            elif aleatorio <= 0.66:
                return c2
            else:
                return c3
        else:
            colas = [c1, c2, c3]
            ordenada = sorted(colas, key=lambda x: x.tamanio())
            minTamanio = ordenada[0].tamanio()
            posiblesCola = [cola for cola in colas if cola.tamanio() == minTamanio]
            
            if len(posiblesCola) > 1:
                return random.choice(posiblesCola)
            else:
                return posiblesCola[0]
    
    while reloj < tms:
        aleatorio = random.random()
        if aleatorio <= (1/frecuencia):
            c = elegirCajero(c1, c2, c3, reloj)
        if cajero == 0 and not c.vacia():
            dato = int(c.suprimir())
            acum += dato
            cant += 1
            cajero = tac
            lista.append(dato)
        else:
            sinAtender +=1
        reloj += 1
        if cajero > 0:
            cajero -= 1
            
    tiempoEspera = acum/cant
    
    print(f"trabajos sin atender: {sinAtender}")
    print(f"tiempo de espera: {tiempoEspera}")
    print(f"cantidad de trabajos: {cant}")
    print(f"lista de tiempos de espera: {lista}")
    print(f"tiempo: {acum}")
    
if __name__ == "__main__":
    main()