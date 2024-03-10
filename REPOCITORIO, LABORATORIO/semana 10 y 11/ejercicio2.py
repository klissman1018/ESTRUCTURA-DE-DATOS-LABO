"Contar Nodos Pares e Impares:"
"2. Crea una lista con al menos 9 nodos, cuenta cuántos nodos tienen un dato par y cuántos tienen un dato impar e imprime la lista hacia adelante y hacia atrás."


# Definición de la clase Nodo para la lista enlazada doble
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None  # Puntero al siguiente nodo
        self.anterior = None  # Puntero al nodo anterior


# Función para contar nodos pares e impares en la lista enlazada doble
def contar_pares_impares(lista):
    nodo_actual = lista
    nodos_pares = 0
    nodos_impares = 0
    while nodo_actual is not None:
        if nodo_actual.dato % 2 == 0:  # Comprobación si el dato es par
            nodos_pares += 1
        else:
            nodos_impares += 1
        nodo_actual = nodo_actual.siguiente
    return nodos_pares, nodos_impares


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


# Crear la lista enlazada doble
nodo1 = Nodo(1)
nodo2 = Nodo(2)
nodo3 = Nodo(3)
nodo4 = Nodo(4)
nodo5 = Nodo(5)
nodo6 = Nodo(6)
nodo7 = Nodo(7)
nodo8 = Nodo(8)
nodo9 = Nodo(9)

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
nodo7.siguiente = nodo8
nodo8.anterior = nodo7
nodo8.siguiente = nodo9
nodo9.anterior = nodo8

# Contar nodos pares e impares
nodos_pares, nodos_impares = contar_pares_impares(nodo1)

# Imprimir la lista hacia adelante y hacia atrás
print("Lista hacia adelante:")
imprimir_adelante(nodo1)
print("Lista hacia atrás:")
imprimir_atras(nodo1)

# Imprimir el número de nodos pares e impares
print("Número de nodos pares:", nodos_pares)
print("Número de nodos impares:", nodos_impares)
