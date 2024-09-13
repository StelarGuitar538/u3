from cola2 import Cola
import random

def main():
    c = Cola()
    tms = 120
    tac = 5
    fre = 5
    
    reloj = 0
    imp = 0
    acum = 0
    cont = 0
    sa = 0
    lista= []
    
    while reloj < tms:
        a = random.random()
        if a <= (1/fre):
            c.insertar(reloj)
            
        if imp == 0 and not c.vacia():
            dato = int(c.suprimir())
            lista.append(dato)
            reloj = tac
            acum +=dato
            cont +=1
        else:
            sa +=1
            
        if imp > 0:
            imp -=1
        reloj +=1
        