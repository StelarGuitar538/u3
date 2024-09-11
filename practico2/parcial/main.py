from cola import Cola
import random

def main():
    c = Cola()
    
    tms = 120
    tae = 15
    fre = 10
    sinAtender = 0
    lista = []
    reloj = 0
    ipv= 0
    acum=0
    cont=0
    
    while reloj < tms:
        a = random.random()
        if a <= (1/fre):
            c.insertar(reloj)
        if ipv == 0 and not c.vacia():
            dato = int(c.suprimir())
            ipv = tae
            acum+= dato
            cont+=1
            lista.append(dato)
        else:
            sinAtender +=1
        reloj +=1
        
        if ipv > 0:
            ipv -= 1
        
    tiempoEspera = acum/cont
    
    print(f"sin atender {sinAtender} tiempo de espera {tiempoEspera} \b cantidad de trabajos: {cont}")

if __name__ == "__main__":
    main()
    