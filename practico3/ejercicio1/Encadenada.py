from nodo import Nodo

class ListaEncadenada:
    def __init__(self):
        self.cabeza = None

    def agregar(self, dato):
        """Agrega un elemento al final de la lista."""
        nuevo_nodo = Nodo(dato)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    def insertar(self, indice, dato):
        """Inserta un elemento en la posición especificada."""
        if indice < 0:
            raise IndexError("Índice fuera de rango")
        nuevo_nodo = Nodo(dato)
        if indice == 0:
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            for _ in range(indice - 1):
                if not actual:
                    raise IndexError("Índice fuera de rango")
                actual = actual.siguiente
            nuevo_nodo.siguiente = actual.siguiente
            actual.siguiente = nuevo_nodo

    def eliminar(self, indice):
        """Elimina un elemento en la posición especificada."""
        if indice < 0 or not self.cabeza:
            raise IndexError("Índice fuera de rango")
        if indice == 0:
            eliminado = self.cabeza.dato
            self.cabeza = self.cabeza.siguiente
            return eliminado
        actual = self.cabeza
        for _ in range(indice - 1):
            if not actual.siguiente:
                raise IndexError("Índice fuera de rango")
            actual = actual.siguiente
        eliminado = actual.siguiente.dato
        actual.siguiente = actual.siguiente.siguiente
        return eliminado

    def obtener(self, indice):
        """Obtiene el elemento en la posición especificada."""
        if indice < 0:
            raise IndexError("Índice fuera de rango")
        actual = self.cabeza
        for _ in range(indice):
            if not actual:
                raise IndexError("Índice fuera de rango")
            actual = actual.siguiente
        if not actual:
            raise IndexError("Índice fuera de rango")
        return actual.dato

    def tamaño(self):
        """Devuelve el número de elementos en la lista."""
        contador = 0
        actual = self.cabeza
        while actual:
            contador += 1
            actual = actual.siguiente
        return contador

    def es_vacia(self):
        """Devuelve True si la lista está vacía, de lo contrario False."""
        return self.cabeza is None

# Ejemplo de uso
lista_encadenada = ListaEncadenada()
lista_encadenada.agregar(10)
lista_encadenada.insertar(1, 20)
print(lista_encadenada.obtener(0))  # Salida: 10
print(lista_encadenada.obtener(1))  # Salida: 20
