"7. Calcula la suma de los números pares en un rango especificado por el usuario."

# Definimos una función llamada suma_numeros_pares que toma dos argumentos: inicio y fin.
def suma_numeros_pares(inicio, fin):
    # Inicializamos una variable suma en 0, que usaremos para acumular la suma de los números pares.
    suma = 0
    # Usamos un bucle for para iterar sobre un rango de números desde el valor de inicio hasta el valor de fin, incluyendo ambos.
    for numero in range(inicio, fin + 1):
        # Dentro del bucle, usamos una condición if para verificar si el número actual es par (divisible por 2 sin residuo).
        if numero % 2 == 0:
            # Si el número es par, lo sumamos a la variable suma.
            suma += numero
    # Después de iterar sobre todos los números, retornamos el valor acumulado en suma.
    return suma

# Solicitamos al usuario que ingrese el número inicial del rango y lo convertimos a entero.
inicio_rango = int(input("Ingrese el número inicial del rango: "))
# Solicitamos al usuario que ingrese el número final del rango y lo convertimos a entero.
fin_rango = int(input("Ingrese el número final del rango: "))

# Llamamos a la función suma_numeros_pares con los valores de inicio_rango y fin_rango, y almacenamos el resultado en la variable resultado.
resultado = suma_numeros_pares(inicio_rango, fin_rango)
# Imprimimos el resultado formateado, mostrando la suma de los números pares en el rango especificado.
print(f"La suma de los números pares en el rango de {inicio_rango} a {fin_rango} es: {resultado}")