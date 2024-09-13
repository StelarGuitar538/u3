from pila import Pila

def decimalABinario(pila, decimal):
    if decimal == 0:
        return "0"
    
    entero = int(decimal)
    
    while entero > 0:
        residuo = entero %2
        pila.inser

def main():
    p = Pila()
    decimal = float(input("ingrese un decimal: "))
    binario = decimalABinario(p, decimal)
    print(f"la parte entera de {decimal} en binario es {binario}")
    
if __name__ == "__main__":
    main()
