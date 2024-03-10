#11.   Implementar una función que encuentre el nodo con el valor máximo en el árbol.

class Nodo:
    # Esta función inicializa un nodo con un valor dado y establece sus hijos izquierdo y derecho como None.
    def __init__(self, valor):
        self.valor = valor  # Almacena el valor del nodo.
        self.izquierdo = None  # Inicializa el hijo izquierdo del nodo como None.
        self.derecho = None  # Inicializa el hijo derecho del nodo como None.

# Esta función busca el nodo con el valor máximo en el árbol binario.
def nodo_maximo(nodo):
    # Si el nodo actual es None, significa que hemos llegado al final del árbol sin encontrar un nodo.
    if nodo is None:
        return None
    # Si el nodo derecho del nodo actual es None, significa que hemos encontrado el nodo máximo.
    elif nodo.derecho is None:
        return nodo
    # Si el nodo tiene un hijo derecho, la función se llama a sí misma con el hijo derecho del nodo actual.
    else:
        return nodo_maximo(nodo.derecho)

# Creación del nodo raíz del árbol binario con valor 50.
nodo_raiz = Nodo(50)
# Asignación del hijo izquierdo del nodo raíz con valor 30.
nodo_raiz.izquierdo = Nodo(30)
# Asignación del hijo derecho del nodo raíz con valor 70.
nodo_raiz.derecho = Nodo(70)
# Asignación del hijo izquierdo del hijo izquierdo del nodo raíz con valor 20.
nodo_raiz.izquierdo.izquierdo = Nodo(20)
# Asignación del hijo derecho del hijo izquierdo del nodo raíz con valor 40.
nodo_raiz.izquierdo.derecho = Nodo(40)
# Asignación del hijo izquierdo del hijo derecho del nodo raíz con valor 60.
nodo_raiz.derecho.izquierdo = Nodo(60)
# Asignación del hijo derecho del hijo derecho del nodo raíz con valor 80.
nodo_raiz.derecho.derecho = Nodo(80)

# Llamada a la función nodo_maximo para encontrar el nodo con el valor máximo en el árbol.
nodo_max = nodo_maximo(nodo_raiz)
# Si se encuentra un nodo máximo, se imprime su valor. De lo contrario, se indica que el árbol está vacío.
if nodo_max:
    print(f"El nodo con el valor máximo es {nodo_max.valor}.")
else:
    print("El árbol está vacío.")
