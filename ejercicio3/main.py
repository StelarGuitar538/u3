from pila import Pila

def factorial(pila, n):
    while n > 0:
        pila.insertar(n)
        n -= 1
    resultado = 1
    while not pila.vacia():
        valor = pila.eliminar()
        resultado *= valor
    return resultado

def main():
    p = Pila()
    n = int(input("Ingrese un numero: "))
    res = factorial(p, n)
    print(f"el factorial de {n} es {res}")
    
if __name__ == "__main__":
    main()