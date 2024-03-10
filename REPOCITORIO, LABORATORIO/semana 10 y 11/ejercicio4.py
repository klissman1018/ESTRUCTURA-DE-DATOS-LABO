"Eliminar Nodos Duplicados:"
"4. Crea una lista con nodos que contengan datos duplicados, elimina todos los nodos duplicados, dejando solo una instancia de cada dato e imprime la lista hacia adelante y hacia atrás."


# Definición de la clase Nodo para la lista enlazada doble
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None  # Puntero al siguiente nodo
        self.anterior = None  # Puntero al nodo anterior


# Función para eliminar nodos duplicados de una lista enlazada doble
def eliminar_nodos_duplicados(lista):
    # Creamos un conjunto para mantener un registro de los datos que ya hemos visto
    datos_vistos = set()
    nodo_actual = lista

    # Recorremos la lista enlazada
    while nodo_actual is not None:
        if (
            nodo_actual.dato in datos_vistos
        ):  # Si el dato ya ha sido visto, eliminamos el nodo
            nodo_anterior.siguiente = nodo_actual.siguiente
            if nodo_actual.siguiente is not None:
                nodo_actual.siguiente.anterior = nodo_anterior
        else:
            datos_vistos.add(
                nodo_actual.dato
            )  # Agregamos el dato al conjunto de datos vistos
            nodo_anterior = nodo_actual  # Actualizamos el nodo anterior
        nodo_actual = nodo_actual.siguiente  # Avanzamos al siguiente nodo

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


# Crear la lista enlazada doble con nodos que contienen datos duplicados
nodo1 = Nodo(1)
nodo2 = Nodo(2)
nodo3 = Nodo(2)
nodo4 = Nodo(3)
nodo5 = Nodo(3)
nodo6 = Nodo(3)
nodo7 = Nodo(4)

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
nodo6.siguiente = nodo7
nodo7.anterior = nodo6

# Eliminar nodos duplicados
lista_sin_duplicados = eliminar_nodos_duplicados(nodo1)

# Imprimir la lista sin duplicados hacia adelante y hacia atrás
print("Lista sin duplicados hacia adelante:")
imprimir_adelante(lista_sin_duplicados)
print("Lista sin duplicados hacia atrás:")
imprimir_atras(lista_sin_duplicados)
