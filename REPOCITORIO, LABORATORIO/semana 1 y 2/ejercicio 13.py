"13. Crea un programa que genere la tabla de multiplicar de un número ingresado por el usuario."

# Esta línea solicita al usuario que ingrese un número y lo convierte a entero. Este número se usará para generar su tabla de multiplicar.
numero = int(input("Ingrese el número para generar su tabla de multiplicar: "))

# Este bucle for recorre un rango de 1 a 12 (inclusive) y para cada valor de 'i' en ese rango, realiza la operación de multiplicación del número ingresado por el usuario (almacenado en la variable 'numero') por 'i', y luego imprime el resultado en el formato "numero x i = resultado".
for i in range(1, 13):
    print(f"{numero} x {i} = {numero * i}")