"Ejercicio 3: Escribe una función recursiva que imprima la pirámide de números del 1 al n."


def imprimir_piramide(n, current=1):
    if current > n:  # Condición de base
        return
    # Imprimir espacios necesarios para alinear los números
    print(" " * (n - current) + " ".join(str(i) for i in range(1, current + 1)))
    # Llamada recursiva para el siguiente nivel
    imprimir_piramide(n, current + 1)


# Solicitar al usuario que ingrese el número de niveles de la pirámide
n = int(input("Ingrese el número de niveles de la pirámide: "))
imprimir_piramide(n)
