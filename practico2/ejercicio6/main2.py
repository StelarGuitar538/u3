from cola2 import Cola
import random

def main():
    c = Cola()
    
    frecuencia = int(input("ingrese frecuencia de llegada de trabajos"))
    tac = int(input("ingrese el tiempo de atencion de la impresora"))
    tms = int(input("tiempo maximo de simulacion"))
    
    impresora = 0
    reloj = 0
    acum = 0
    cant = 0
    sinAtender = 0
    lista = []
    
    while reloj < tms:
        aleatorio = random.random()
        if aleatorio <= (1/frecuencia):
            c.insertar(reloj)
        if impresora == 0 and not c.vacia():
            dato = int(c.suprimir())
            acum += dato
            cant +=1
            impresora = tac
            lista.append(dato)
        else:
            sinAtender += 1
        reloj += 1
        if impresora > 0:
            impresora -= 1
    
    tiempoEspera = acum/cant
    
    print(f"trabajos sin atender: {sinAtender}")
    print(f"tiempo de espera: {tiempoEspera}")
    
if __name__ == "__main__":
    main()