from pila import Pila

def main():
    p = Pila()
    decimal = float(input("ingrese un decimal: "))
    binairo = p.decimalABinario(decimal)
    print(f"la parte entera de {decimal} en binario es {binairo}")
    
if __name__ == "__main__":
    main()