"Invertir la Lista:"
"5. Crea una lista con al menos 6 nodos, invierte el orden de la lista (el último elemento se convierte en el primero y viceversa) e imprime la lista hacia adelante y hacia atrás."


# Definición de la clase Nodo para la lista enlazada doble
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None  # Puntero al siguiente nodo
        self.anterior = None  # Puntero al nodo anterior


# Función para invertir el orden de una lista enlazada doble
def invertir_lista(lista):
    nodo_actual = lista
    while nodo_actual is not None:
        # Intercambiamos los punteros del nodo actual
        nodo_actual.anterior, nodo_actual.siguiente = (
            nodo_actual.siguiente,
            nodo_actual.anterior,
        )
        # Movemos al siguiente nodo
        nodo_actual = nodo_actual.anterior

    # El nodo anterior al nodo actual al final de la inversión será el nuevo nodo inicial
    if nodo_actual is None:
        lista = lista.anterior

    return lista


# Función para imprimir la lista enlazada doble hacia adelante
def imprimir_adelante(lista):
    nodo_actual = lista
    while nodo_actual is not None:
        print(nodo_actual.dato, end=" ")
        nodo_actual = nodo_actual.siguiente
    print()


# Función para imprimir la lista enlazada doble hacia atrás
def imprimir_atras(lista):
    nodo_actual = lista
    while nodo_actual.siguiente is not None:
        nodo_actual = nodo_actual.siguiente
    while nodo_actual is not None:
        print(nodo_actual.dato, end=" ")
        nodo_actual = nodo_actual.anterior
    print()


# Crear la lista enlazada doble con al menos 6 nodos
nodo1 = Nodo(1)
nodo2 = Nodo(2)
nodo3 = Nodo(3)
nodo4 = Nodo(4)
nodo5 = Nodo(5)
nodo6 = Nodo(6)

nodo1.siguiente = nodo2
nodo2.anterior = nodo1
nodo2.siguiente = nodo3
nodo3.anterior = nodo2
nodo3.siguiente = nodo4
nodo4.anterior = nodo3
nodo4.siguiente = nodo5
nodo5.anterior = nodo4
nodo5.siguiente = nodo6
nodo6.anterior = nodo5

# Invertir el orden de la lista
lista_invertida = invertir_lista(nodo1)

# Imprimir la lista invertida hacia adelante y hacia atrás
print("Lista invertida hacia adelante:")
imprimir_adelante(lista_invertida)
print("Lista invertida hacia atrás:")
imprimir_atras(lista_invertida)
