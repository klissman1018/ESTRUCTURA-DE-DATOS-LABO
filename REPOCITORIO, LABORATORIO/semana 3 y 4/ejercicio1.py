"Ejercicio 1: Escribe una función recursiva que imprima los números pares del 1 al 100."


def imprimir_par(n=2):
    if n <= 100:  # Verifica si el número actual es menor o igual a 100
        print(n)  # Imprime el número par actual
        imprimir_par(
            n + 2
        )  # Llama a la función recursivamente con el siguiente número par


imprimir_par()  # Inicia la función con el primer número par
