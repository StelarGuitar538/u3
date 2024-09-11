from cola import Cola 
import random

def main():
    c= Cola()
    tms = 120
    fre = 10
    tae = 15
    
    reloj = 0
    acum =0
    cont = 0
    sinAtender = 0
    lista = []
    ipv = 0
    
    while reloj <= tms:
        a = random.random()
        if a <= (1/fre):
            c.insertar(reloj)
        
        if ipv == 0 and not c.vacia(): 
            dato = int(c.suprimir()) #suprimir elemento de la cola
            acum += dato
            cont +=1
            ipv = tae
            lista.append(dato)
        else:
            sinAtender+=1
        reloj +=1
        
        if ipv > 0:
            ipv -=1
        
    te = acum/cont
    
    print(f"tiempo de espera: {te}")
    print(f"tiempo: {acum}")
    print(f"cantidad de trabajos: {cont}")
    print(f"lista de tiempos de espera: {lista}")
    print(f"trabajos sin atender: {sinAtender}")
    
if __name__ == "__main__":
    main()
        
        
            