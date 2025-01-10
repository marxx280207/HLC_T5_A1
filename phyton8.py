base = int(input("Introduce la base del triángulo en metros: "))
altura = int(input("Introduce la altura del triángulo en metros: "))
precio = int(input("Introduce el precio por metro cuadrado: "))

area = (base*altura) / 2

total = area*precio

print(f"Área = {area} metros cuadrados.")
print(f"Costo total = {total} unidades.")

