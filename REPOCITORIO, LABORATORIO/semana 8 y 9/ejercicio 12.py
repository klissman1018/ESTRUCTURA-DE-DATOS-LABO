"12. Crea una función que devuelva la longitud de una lista enlazada simple."


# Definición de la clase Nodo con su constructor y atributos
class Nodo:
    def __init__(self, valor):
        self.valor = valor  # Asigna el valor al atributo 'valor' del nodo
        self.siguiente = None  # Inicializa el atributo 'siguiente' como None


# Definición de la clase ListaEnlazada con su constructor y atributos
class ListaEnlazada:
    def __init__(self):
        self.cabeza = None  # Inicializa el atributo 'cabeza' como None

    # Método para agregar un nuevo nodo a la lista enlazada
    def agregar_elemento(self, valor):
        nuevo_nodo = Nodo(valor)  # Crea un nuevo nodo con el valor proporcionado
        nuevo_nodo.siguiente = (
            self.cabeza
        )  # Establece el siguiente del nuevo nodo como la cabeza actual
        self.cabeza = nuevo_nodo  # Actualiza la cabeza de la lista con el nuevo nodo

    # Método para obtener la longitud de la lista enlazada
    def longitud_lista(self):
        longitud = 0  # Inicializa la longitud en 0
        actual = self.cabeza  # Inicializa el nodo actual como la cabeza de la lista
        while actual:  # Itera sobre la lista mientras haya nodos
            longitud += 1  # Incrementa la longitud en 1
            actual = actual.siguiente  # Avanza al siguiente nodo
        return longitud  # Retorna la longitud de la lista


# Ejemplo de uso
mi_lista = ListaEnlazada()  # Crea una nueva lista enlazada
mi_lista.agregar_elemento(3)  # Agrega un nodo con valor 3 a la lista
mi_lista.agregar_elemento(7)  # Agrega un nodo con valor 7 a la lista
mi_lista.agregar_elemento(1)  # Agrega un nodo con valor 1 a la lista

longitud = mi_lista.longitud_lista()  # Obtiene la longitud de la lista
print("Longitud de la lista enlazada:", longitud)  # Imprime la longitud de la lista
