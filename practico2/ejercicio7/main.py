from cola import Cola
import random

def main():
    c1 = Cola()
    c2 = Cola()
    c3 = Cola()
    
    # Frecuencia de atención de los cajeros
    frecuencia1 = 5
    frecuencia2 = 3
    frecuencia3 = 4

    # Frecuencia de llegada de los clientes y tiempo de simulación
    tac = 2
    tms = 120
    
    # Tiempo restante para cada cajero
    cajero1 = 0
    cajero2 = 0
    cajero3 = 0

    # Variables para control de la simulación
    reloj = 0
    acum = 0
    cant = 0
    sinAtender = 0
    lista = []
    
    # Función para elegir a qué cajero irá el cliente
    def elegirCajero(c1, c2, c3):
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
    
    # Simulación del tiempo
    while reloj < tms:
        # Generar un cliente cada tac minutos
        if reloj % tac == 0:
            c = elegirCajero(c1, c2, c3)
            c.insertar(reloj)
        
        # Atender clientes en cada cajero
        if cajero1 == 0 and not c1.vacia():
            tiempo_espera = reloj - c1.suprimir()
            acum += tiempo_espera
            cant += 1
            lista.append(tiempo_espera)
            cajero1 = frecuencia1
        elif cajero2 == 0 and not c2.vacia():
            tiempo_espera = reloj - c2.suprimir()
            acum += tiempo_espera
            cant += 1
            lista.append(tiempo_espera)
            cajero2 = frecuencia2
        elif cajero3 == 0 and not c3.vacia():
            tiempo_espera = reloj - c3.suprimir()
            acum += tiempo_espera
            cant += 1
            lista.append(tiempo_espera)
            cajero3 = frecuencia3

        # Decrementar los tiempos de atención de los cajeros
        if cajero1 > 0:
            cajero1 -= 1
        if cajero2 > 0:
            cajero2 -= 1
        if cajero3 > 0:
            cajero3 -= 1

        reloj += 1

    # Resultados
    tiempoEspera = acum / cant if cant > 0 else 0
    
    print(f"Clientes sin atender: {sinAtender}")
    print(f"Tiempo promedio de espera: {tiempoEspera:.2f} minutos")
    print(f"Cantidad de clientes atendidos: {cant}")
    print(f"Clientes atendidos por cajero: {lista}")
    
if __name__ == "__main__":
    main()


#o(tms)