from nodo import Nodo

class ListaOrdenadaEncadenada:
    def __init__(self):
        self.cabeza = None

    def agregar(self, dato):
        """Agrega un elemento en la posición ordenada correcta."""
        nuevo_nodo = Nodo(dato)
        # Si la lista está vacía o el dato es menor que el de la cabeza, se inserta al principio
        if not self.cabeza or self.cabeza.dato >= dato:
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza = nuevo_nodo
        else:
            # Encuentra la posición correcta para insertar
            actual = self.cabeza
            while actual.siguiente and actual.siguiente.dato < dato:
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
lista_ordenada_encadenada = ListaOrdenadaEncadenada()
lista_ordenada_encadenada.agregar(20)
lista_ordenada_encadenada.agregar(10)
lista_ordenada_encadenada.agregar(30)
print(lista_ordenada_encadenada.obtener(0))  # Salida: 10
print(lista_ordenada_encadenada.obtener(1))  # Salida: 20
print(lista_ordenada_encadenada.obtener(2))  # Salida: 30
