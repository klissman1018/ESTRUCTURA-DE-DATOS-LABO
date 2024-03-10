"3. Pide la base y la altura de un triángulo al usuario y calcula su área."

base = float(input("Ingrese la base del triángulo: "))  # Esta línea solicita al usuario que ingrese la base del triángulo y convierte el valor ingresado a tipo flotante.
altura = float(input("Ingrese la altura del triángulo: "))  # Esta línea solicita al usuario que ingrese la altura del triángulo y convierte el valor ingresado a tipo flotante.

area_triangulo = 0.5 * base * altura  # Esta línea calcula el área del triángulo utilizando la fórmula (base * altura) / 2.

print(f"El área del triángulo con base {base} y altura {altura} es: {area_triangulo}")  # Esta línea imprime el área calculada del triángulo, mostrando también los valores de base y altura ingresados por el usuario.