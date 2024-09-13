from cola import Cola
import random

def main():
    c1 = Cola()
    c2 = Cola()
    c3 = Cola()
    
    fre1 = 5
    fre2 = 3
    fre3  =4
    
    tac = 2
    tms = 120
    
    cajero1 = 0
    cajero2 = 0
    cajero3 = 0
    
    reloj = 0
    sa = 0
    acum = 0
    cont = 0
    lista = []
    
    
    def elegirCajero(c1, c2, c3):
        if c1.vacia() and c2.vacia() and c3.vacia():
            a = random.random()
            if a <= 0.33:
                return c1
            elif a <= 0.66:
                return c2
            else:
                return c3
        else:
            colas = [c1, c2, c3]
            ordenada = sorted(colas, key=lambda x: x.tamanio())
            mintamanio = ordenada[0].tamanio()
            posibleCola = [cola for cola in colas if cola.tamanio() == mintamanio]
            
            if len(posibleCola) > 1:
                return random.choice(posibleCola)
            else:
                return posibleCola[0]