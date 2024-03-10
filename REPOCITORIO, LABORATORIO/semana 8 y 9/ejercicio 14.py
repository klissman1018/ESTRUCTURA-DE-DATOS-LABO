"Eliminar Duplicados"
"14. Crea una función que elimine los nodos duplicados de una lista enlazada simple."


class Nodo:
    # Define la clase Nodo con un constructor que recibe un valor
    def __init__(self, valor):
        # Inicializa el valor del nodo con el valor recibido
        self.valor = valor
        # Inicializa el siguiente nodo como None
        self.siguiente = None

class ListaEnlazada:
    # Define la clase ListaEnlazada con un constructor
    def __init__(self):
        # Inicializa la cabeza de la lista como None
        self.cabeza = None

    # Función para agregar un elemento a la lista enlazada
    def agregar_elemento(self, valor):
        # Crea un nuevo nodo con el valor recibido
        nuevo_nodo = Nodo(valor)
        # El siguiente del nuevo nodo apunta a la cabeza actual de la lista
        nuevo_nodo.siguiente = self.cabeza
        # La cabeza de la lista se actualiza al nuevo nodo
        self.cabeza = nuevo_nodo

    # Función para eliminar duplicados en la lista enlazada
    def eliminar_duplicados(self):
        # Conjunto para almacenar los valores vistos
        valores_vistos = set()
        # Nodo actual comienza en la cabeza de la lista
        actual = self.cabeza
        # Nodo anterior se inicializa como None
        anterior = None

        # Recorre la lista mientras haya nodos
        while actual:
            # Verifica si el valor actual ya ha sido visto
            if actual.valor in valores_vistos:
                # Si es un duplicado, elimina el nodo actual
                anterior.siguiente = actual.siguiente
            else:
                # Si es un valor nuevo, lo agrega al conjunto de valores vistos y actualiza el nodo anterior
                valores_vistos.add(actual.valor)
                anterior = actual

            # Avanza al siguiente nodo en la lista
            actual = actual.siguiente

mi_lista = ListaEnlazada()
mi_lista.agregar_elemento(3)
mi_lista.agregar_elemento(7)
mi_lista.agregar_elemento(3)
mi_lista.agregar_elemento(1)
mi_lista.agregar_elemento(7)

print("Lista enlazada original:")
actual = mi_lista.cabeza
while actual:
    # Imprime el valor del nodo actual
    print(actual.valor, end=" ")
    # Avanza al siguiente nodo
    actual = actual.siguiente

mi_lista.eliminar_duplicados()

print("\nLista enlazada después de eliminar duplicados:")
actual = mi_lista.cabeza
while actual:
    # Imprime el valor del nodo actual después de eliminar duplicados
    print(actual.valor, end=" ")
    # Avanza al siguiente nodo
    actual = actual.siguiente
