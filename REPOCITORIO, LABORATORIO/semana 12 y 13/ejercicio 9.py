#9.    Implementar una función que calcule la profundidad de un nodo (la longitud del camino desde la raíz 
#hasta el nodo).

class Nodo:
    # Constructor de la clase Nodo, inicializa un nodo con un valor dado y sus hijos izquierdo y derecho como None.
    def __init__(self, valor):
        self.valor = valor  # Almacena el valor del nodo.
        self.izquierdo = None  # Inicializa el hijo izquierdo del nodo como None.
        self.derecho = None  # Inicializa el hijo derecho del nodo como None.

# Función para calcular la profundidad de un nodo dado un valor.
def profundidad_nodo(nodo, valor, profundidad=0):
    # Si el nodo actual es None, significa que el valor no se encuentra en el árbol.
    if nodo is None:
        return -1 
    # Si el valor del nodo actual coincide con el valor buscado, retorna la profundidad actual.
    if nodo.valor == valor:
        return profundidad 
    # Busca en el subárbol izquierdo y aumenta la profundidad en 1.
    izquierda = profundidad_nodo(nodo.izquierdo, valor, profundidad + 1)
    # Si encuentra el valor en el subárbol izquierdo, retorna la profundidad.
    if izquierda != -1:
        return izquierda 
    # Si no se encuentra en el subárbol izquierdo, busca en el subárbol derecho y aumenta la profundidad en 1.
    return profundidad_nodo(nodo.derecho, valor, profundidad + 1) 

# Creación del árbol de nodos manualmente.
nodo_raiz = Nodo(1)  # Nodo raíz con valor 1.
nodo_raiz.izquierdo = Nodo(2)  # Hijo izquierdo del nodo raíz con valor 2.
nodo_raiz.derecho = Nodo(3)  # Hijo derecho del nodo raíz con valor 3.
nodo_raiz.izquierdo.izquierdo = Nodo(4)  # Hijo izquierdo del hijo izquierdo del nodo raíz con valor 4.
nodo_raiz.izquierdo.derecho = Nodo(5)  # Hijo derecho del hijo izquierdo del nodo raíz con valor 5.

# Valor que se desea buscar en el árbol.
valor_buscado = 5
# Llamada a la función para calcular la profundidad del nodo con el valor buscado.
profundidad = profundidad_nodo(nodo_raiz, valor_buscado)
# Si la profundidad es diferente de -1, significa que el valor se encontró en el árbol.
if profundidad != -1:
    print(f"La profundidad del nodo con valor {valor_buscado} es {profundidad}.")
else:
    # Si la profundidad es -1, significa que el valor no se encontró en el árbol.
    print(f"El nodo con valor {valor_buscado} no se encuentra en el árbol.")
