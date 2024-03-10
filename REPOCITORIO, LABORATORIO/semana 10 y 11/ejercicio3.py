"Insertar Nodo en Posición Específica:"
"3. Crea una lista con al menos 5 nodos, inserta un nuevo nodo con el dato 15 en la posición 3 e imprime la lista hacia adelante y hacia atrás."


# Definición de la clase Nodo para la lista enlazada doble
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None  # Puntero al siguiente nodo
        self.anterior = None  # Puntero al nodo anterior


# Función para insertar un nuevo nodo en una posición específica de la lista enlazada doble
def insertar_nodo_en_posicion(lista, dato, posicion):
    nuevo_nodo = Nodo(dato)
    if posicion == 1:  # Si la posición es la primera
        nuevo_nodo.siguiente = lista
        if lista is not None:
            lista.anterior = nuevo_nodo
        return nuevo_nodo
    else:
        nodo_actual = lista
        contador = 1
        while nodo_actual is not None and contador < posicion - 1:
            nodo_actual = nodo_actual.siguiente
            contador += 1
        if (
            nodo_actual is None
        ):  # Si la posición excede el tamaño de la lista, se inserta al final
            nodo_actual = lista
            while nodo_actual.siguiente is not None:
                nodo_actual = nodo_actual.siguiente
            nodo_actual.siguiente = nuevo_nodo
            nuevo_nodo.anterior = nodo_actual
        else:  # Si la posición está en medio de la lista
            nuevo_nodo.siguiente = nodo_actual.siguiente
            if nodo_actual.siguiente is not None:
                nodo_actual.siguiente.anterior = nuevo_nodo
            nodo_actual.siguiente = nuevo_nodo
            nuevo_nodo.anterior = nodo_actual
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


# Crear la lista enlazada doble con al menos 5 nodos
nodo1 = Nodo(1)
nodo2 = Nodo(2)
nodo3 = Nodo(3)
nodo4 = Nodo(4)
nodo5 = Nodo(5)

nodo1.siguiente = nodo2
nodo2.anterior = nodo1
nodo2.siguiente = nodo3
nodo3.anterior = nodo2
nodo3.siguiente = nodo4
nodo4.anterior = nodo3
nodo4.siguiente = nodo5
nodo5.anterior = nodo4

# Insertar un nuevo nodo con el dato 15 en la posición 3
lista = insertar_nodo_en_posicion(nodo1, 15, 3)

# Imprimir la lista hacia adelante y hacia atrás
print("Lista hacia adelante:")
imprimir_adelante(lista)
print("Lista hacia atrás:")
imprimir_atras(lista)
