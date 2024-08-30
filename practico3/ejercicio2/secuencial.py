import numpy as np

class ListaOrdenadaSecuencial:
    def __init__(self, capacidad_inicial=10):
        self.lista = np.empty(capacidad_inicial, dtype=object)
        self.tamaño_actual = 0
        self.capacidad = capacidad_inicial

    def _redimensionar(self, nueva_capacidad):
        """Redimensiona el array a una nueva capacidad."""
        nueva_lista = np.empty(nueva_capacidad, dtype=object)
        for i in range(self.tamaño_actual):
            nueva_lista[i] = self.lista[i]
        self.lista = nueva_lista
        self.capacidad = nueva_capacidad

    def agregar(self, elemento):
        """Agrega un elemento en la posición ordenada correcta."""
        if self.tamaño_actual == self.capacidad:
            self._redimensionar(self.capacidad * 2)

        # Encuentra la posición donde insertar el nuevo elemento
        indice = 0
        while indice < self.tamaño_actual and self.lista[indice] < elemento:
            indice += 1
        
        # Mueve los elementos para hacer espacio
        for i in range(self.tamaño_actual, indice, -1):
            self.lista[i] = self.lista[i - 1]

        # Inserta el nuevo elemento
        self.lista[indice] = elemento
        self.tamaño_actual += 1

    def eliminar(self, indice):
        """Elimina un elemento en la posición especificada."""
        if indice < 0 or indice >= self.tamaño_actual:
            raise IndexError("Índice fuera de rango")
        eliminado = self.lista[indice]
        for i in range(indice, self.tamaño_actual - 1):
            self.lista[i] = self.lista[i + 1]
        self.tamaño_actual -= 1
        if self.tamaño_actual <= self.capacidad // 4 and self.capacidad > 10:
            self._redimensionar(self.capacidad // 2)
        return eliminado

    def obtener(self, indice):
        """Obtiene el elemento en la posición especificada."""
        if indice < 0 or indice >= self.tamaño_actual:
            raise IndexError("Índice fuera de rango")
        return self.lista[indice]

    def tamaño(self):
        """Devuelve el número de elementos en la lista."""
        return self.tamaño_actual

    def es_vacia(self):
        """Devuelve True si la lista está vacía, de lo contrario False."""
        return self.tamaño_actual == 0

# Ejemplo de uso
lista_ordenada_numpy = ListaOrdenadaSecuencial()
lista_ordenada_numpy.agregar(20)
lista_ordenada_numpy.agregar(10)
lista_ordenada_numpy.agregar(30)
print(lista_ordenada_numpy.obtener(0))  # Salida: 10
print(lista_ordenada_numpy.obtener(1))  # Salida: 20
print(lista_ordenada_numpy.obtener(2))  # Salida: 30
