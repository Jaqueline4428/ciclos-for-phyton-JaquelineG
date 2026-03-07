#ejercicio10.py
# Nombre: Jaqueline Gutierrez
# Fecha: 28/02/2026

# Pseudocódigo
# Pedir cantidad de productos N
# total = 0
# Para i desde 1 hasta N
#   pedir precio
#   total = total + precio
# Mostrar total

n = int(input("¿Cuántos productos ingresará?: "))
total = 0

for i in range(n):
    precio = float(input("Ingrese el precio del producto: "))
    total += precio

print("Total a pagar:", total)