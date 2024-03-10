"15. Implementa una función que invierta el orden de una lista enlazada simple."


class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None  # Establece el siguiente nodo como None


def invertir_lista(lista):
    # Inicializando los valores
    prev = None  # Nodo previo inicializado como None
    curr = lista.cabeza  # Nodo actual es la cabeza de la lista
    nex = (
        curr.siguiente if curr else None
    )  # Siguiente nodo es el siguiente de la cabeza si existe, de lo contrario None

    # Recorriendo la lista y ajustando los punteros
    while curr:
        # Invirtiendo el enlace
        curr.siguiente = prev  # El siguiente del nodo actual apunta al nodo previo

        # Moviendo al siguiente nodo
        prev = curr  # El nodo previo ahora es el nodo actual
        curr = nex  # El nodo actual ahora es el siguiente nodo
        if nex:
            nex = (
                nex.siguiente
            )  # Si existe un siguiente nodo, avanzar al siguiente nodo

    # Inicializando la cabeza de la lista invertida
    lista.cabeza = prev  # La cabeza de la lista ahora es el último nodo invertido


class ListaEnlazada:
    def __init__(self):
        self.cabeza = None  # Inicializa la cabeza de la lista como None

    def insertar_final(self, valor):
        nuevo_nodo = Nodo(valor)  # Crea un nuevo nodo con el valor proporcionado
        if self.cabeza is None:
            self.cabeza = nuevo_nodo  # Si la lista está vacía, el nuevo nodo se convierte en la cabeza
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo  # Conecta el nuevo nodo al final de la lista

    def imprimir_lista(self):
        actual = self.cabeza
        while actual:
            print(
                actual.valor, end=" -> "
            )  # Imprime el valor del nodo seguido de una flecha
            actual = actual.siguiente
        print("None")  # Imprime None al final de la lista


def main():
    lista = ListaEnlazada()
    lista.insertar_final(1)
    lista.insertar_final(2)
    lista.insertar_final(3)

    print("Lista original:")
    lista.imprimir_lista()

    invertir_lista(lista)

    print("Lista invertida:")
    lista.imprimir_lista()


if __name__ == "__main__":
    main()
