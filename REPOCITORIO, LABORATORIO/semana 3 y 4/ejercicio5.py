"Ejercicio 2: Escribe una función recursiva que imprima la tabla de multiplicar del n."


# Definimos una función llamada imprimir_tabla_multiplicar que toma dos argumentos: n e i. 
# n es el número del cual queremos imprimir la tabla de multiplicar, e i es el contador que inicia en 1 por defecto.
def imprimir_tabla_multiplicar(n, i=1):
    # Esta condición verifica si el contador i ha superado el valor de 12, que es el límite para imprimir la tabla de multiplicar.
    if i > 12:  
        return  # Si i es mayor que 12, la función termina y no retorna nada.
    # Si i no es mayor que 12, se imprime la multiplicación actual de n por i.
    print(f"{n} x {i} = {n * i}")  
    # Llamamos recursivamente a la misma función, incrementando el valor de i en 1, para imprimir el siguiente valor de la tabla de multiplicar.
    imprimir_tabla_multiplicar(n, i + 1)  #

# Solicitamos al usuario que ingrese un número mediante la función input, convertimos ese valor a entero con int() y lo almacenamos en la variable n.
n = int(input("Ingrese un número: "))
# Llamamos a la función imprimir_tabla_multiplicar pasando como argumento el número ingresado por el usuario.
imprimir_tabla_multiplicar(n)
