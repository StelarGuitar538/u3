from cola import Cola
import random

def main():
    c1 = Cola()
    c2 = Cola()
    c3 = Cola()
    
    frecuencia1 = 5
    frecuencia2 = 3
    frecuencia3 = 4
    tpll = 2
    ts = 120
    
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
            posiblesColas = [cola for cola in colas if cola.tamanio() == minTamanio]
            
            if len(posiblesColas) > 1:
                return random.choice(pos)
    