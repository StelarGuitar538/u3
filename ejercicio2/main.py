from ejercicio4.pila import Pila

def decimalABinario(pila, decimal):
    if decimal == 0:
        return "0"
    
    entero = int(decimal)
    
    while entero > 0:
        residuo = entero % 2
        pila.insertar(residuo)
        entero //= 2
    
    binario = ""
    while not pila.vacia():
        binario += str(pila.suprimir())
    
    return binario[::-1]

def main():
    p = Pila()
    decimal = float(input("Ingrese un decimal: "))
    binario = decimalABinario(p, decimal)
    print(f"La parte entera de {decimal} en binario es {binario}")

if __name__ == "__main__":
    main()
