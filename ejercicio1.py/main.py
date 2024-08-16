from listaEncadenada import Lista

def main():
    l = Lista()
    l.insertarAlInicio(10)
    l.insertarAlInicio(5)
    l.insertarAlFinal(20)
    l.insertarAlFinal(30)
    
    l.mostrar()
    
    print(f"elemento eliminado al inicio: {l.suprimirAlInicio()}")
    
    l.mostrar()
    
    print(f"elemento eliminado al final: {l.suprimirAlFinal()}")
    
    l.mostrar()
    
if __name__ == "__main__":
    main()