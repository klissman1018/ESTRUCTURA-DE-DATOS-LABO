"4. Crea una función que calcule la factorial de un número"

# Solicita al usuario que ingrese un número para calcular su factorial y lo convierte a entero.
numero_factorial = int(input("Ingrese un número para calcular su factorial: "))

# Establece el valor inicial de la variable 'resultado' en 1. Esta variable se usará para almacenar el resultado final del cálculo del factorial.
resultado = 1
# Utiliza un bucle for para iterar sobre una secuencia de números desde 1 hasta el número ingresado por el usuario (incluyéndolo).
# En cada iteración, multiplica el valor actual de 'resultado' por el número de la iteración actual (i) para calcular el factorial.
for i in range(1, numero_factorial + 1):
    resultado *= i

# Muestra el resultado del cálculo del factorial del número ingresado por el usuario, formateando la salida para incluir el número y su factorial.
print(f"El factorial de {numero_factorial} es: {resultado}")
