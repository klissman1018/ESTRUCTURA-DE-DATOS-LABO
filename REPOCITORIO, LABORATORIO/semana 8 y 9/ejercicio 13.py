"13. Implementa una función que concatene dos listas enlazadas simples."

# Definición de la clase Nodo con su constructor y atributos
class Nodo:
    def __init__(self, valor):
        self.valor = valor  # Asigna el valor al atributo 'valor' del nodo
        self.proximo = None  # Inicializa el atributo 'proximo' como None


# Definición de la clase ListaEnlazada con su constructor y atributos
class ListaEnlazada:
    def __init__(self):
        self.primero = None  # Inicializa el atributo 'primero' como None
        self.largo = 0  # Inicializa el atributo 'largo' en 0

    # Método para agregar un nuevo nodo a la lista enlazada
    def agregar(self, valor):
        nodo = Nodo(valor)  # Crea un nuevo nodo con el valor proporcionado
        if self.largo == 0:  # Verifica si la lista está vacía
            self.primero = (
                nodo  # Establece el nuevo nodo como el primero si la lista está vacía
            )
        else:
            actual = self.primero
            while actual.proximo:  # Recorre la lista hasta el último nodo
                actual = actual.proximo
            actual.proximo = nodo  # Conecta el nuevo nodo al último nodo de la lista
        self.largo += 1  # Incrementa el largo de la lista en 1

    # Método para concatenar dos listas enlazadas simples
    def concatenar(self, lista2):
        if self.largo == 0:  # Verifica si la lista actual está vacía
            self.primero = (
                lista2.primero
            )  # Establece la cabeza de la lista actual como la cabeza de la segunda lista
        else:
            actual = self.primero
            while actual.proximo:  # Recorre la lista actual hasta el último nodo
                actual = actual.proximo
            actual.proximo = (
                lista2.primero
            )  # Conecta la segunda lista al final de la lista actual
        self.largo += (
            lista2.largo
        )  # Incrementa el largo de la lista actual por la longitud de la segunda lista


# Función principal para probar la concatenación de listas enlazadas
def principal():
    lista1 = ListaEnlazada()  # Crea una nueva lista enlazada
    lista1.agregar(1)  # Agrega nodos a la primera lista
    lista1.agregar(2)
    lista1.agregar(3)

    lista2 = ListaEnlazada()  # Crea otra lista enlazada
    lista2.agregar(4)  # Agrega nodos a la segunda lista
    lista2.agregar(5)
    lista2.agregar(6)

    lista1.concatenar(lista2)  # Concatena la segunda lista a la primera

    actual = (
        lista1.primero
    )  # Inicializa el nodo actual como el primero de la lista concatenada
    while actual:  # Itera sobre todos los nodos de la lista concatenada
        print(actual.valor)  # Imprime el valor del nodo actual
        actual = actual.proximo  # Avanza al siguiente nodo


if __name__ == "__main__":
    principal()  # Llama a la función principal para probar la concatenación de listas enlazadas
