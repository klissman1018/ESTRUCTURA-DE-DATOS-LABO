"Ejercicio parte 01 – Listas Enlazadas Dobles:"
"Duplicar Nodos:"
"1. Crea una lista con al menos 4 nodos, duplica cada nodo de la lista e imprime la lista original y la lista duplicada hacia adelante y hacia atrás."

class Nodo:
    # Definición de la clase Nodo que representa un nodo de una lista doblemente enlazada
    def __init__(self, dato):
        # Método especial de inicialización de un nodo con un dato dado
        self.dato = dato
        self.siguiente = None  
        self.anterior = None  

def duplicar_nodos(lista):
    # Función que duplica los nodos de una lista doblemente enlazada
    nodo_actual = lista
    while nodo_actual is not None:
        nuevo_nodo = Nodo(nodo_actual.dato)
        nuevo_nodo.siguiente = nodo_actual.siguiente
        nuevo_nodo.anterior = nodo_actual
        nodo_actual.siguiente = nuevo_nodo
        if nuevo_nodo.siguiente is not None:
            nuevo_nodo.siguiente.anterior = nuevo_nodo
        nodo_actual = nuevo_nodo.siguiente

def imprimir_adelante(lista):
    # Función que imprime los datos de una lista doblemente enlazada en orden ascendente
    nodo_actual = lista
    while nodo_actual is not None:
        print(nodo_actual.dato, end=" ")
        nodo_actual = nodo_actual.siguiente
    print()

def imprimir_atras(lista):
    # Función que imprime los datos de una lista doblemente enlazada en orden descendente
    nodo_actual = lista
    while nodo_actual.siguiente is not None:
        nodo_actual = nodo_actual.siguiente
    while nodo_actual is not None:
        print(nodo_actual.dato, end=" ")
        nodo_actual = nodo_actual.anterior
    print()

nodo1 = Nodo(1)
nodo2 = Nodo(2)
nodo3 = Nodo(3)
nodo4 = Nodo(4)

nodo1.siguiente = nodo2
nodo2.anterior = nodo1
nodo2.siguiente = nodo3
nodo3.anterior = nodo2
nodo3.siguiente = nodo4
nodo4.anterior = nodo3

duplicar_nodos(nodo1)

print("Lista Original hacia adelante:")
imprimir_adelante(nodo1)
print("Lista Original hacia atrás:")
imprimir_atras(nodo1)

print("Lista Duplicada hacia adelante:")
imprimir_adelante(nodo1)
print("Lista Duplicada hacia atrás:")
imprimir_atras(nodo1)
