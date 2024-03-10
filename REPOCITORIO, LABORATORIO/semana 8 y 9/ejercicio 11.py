"1.1 Implementa una función que sume todos los nodos de una lista enlazada simple."


# Definir la clase Nodo con su constructor y atributos
class Nodo:
    def __init__(self, valor):
        self.valor = valor  # Asignar el valor al atributo 'valor' del nodo
        self.siguiente = None  # Inicializar el atributo 'siguiente' como None


# Definir la clase ListaEnlazada con su constructor y atributos
class ListaEnlazada:
    def __init__(self):
        self.cabeza = None  # Inicializar el atributo 'cabeza' como None

    # Método para agregar un nuevo nodo a la lista enlazada
    def agregar(self, valor):
        nuevo_nodo = Nodo(valor)  # Crear un nuevo nodo con el valor proporcionado
        if self.cabeza is None:  # Verificar si la lista está vacía
            self.cabeza = nuevo_nodo  # Establecer el nuevo nodo como la cabeza si la lista está vacía
        else:
            actual = self.cabeza
            while actual.siguiente:  # Recorrer la lista hasta el último nodo
                actual = actual.siguiente
            actual.siguiente = (
                nuevo_nodo  # Conectar el nuevo nodo al último nodo de la lista
            )

    # Método para sumar los valores de todos los nodos en la lista
    def sumar_valores(self):
        suma = 0  # Inicializar la variable suma en 0
        actual = self.cabeza
        while actual:  # Iterar sobre todos los nodos de la lista
            suma += actual.valor  # Sumar el valor del nodo actual a la suma total
            actual = actual.siguiente  # Mover al siguiente nodo
        return suma  # Devolver la suma total de los valores de los nodos


# Crear una lista enlazada y agregar algunos nodos
lista = ListaEnlazada()
lista.agregar(4)
lista.agregar(2)
lista.agregar(7)

# Sumar los valores de todos los nodos en la lista
suma = lista.sumar_valores()
print(suma)  # Imprimir la suma total de los valores de los nodos, que será 13
