#ejercicio05.py
# Nombre: Jaqueline Gutierrez
# Fecha: 28/02/2026

# Pseudocódigo
# Pedir N
# suma = 0
# Para i desde 1 hasta N
#   suma = suma + i
# Mostrar suma

n = int(input("Ingrese un número: "))
suma = 0

for i in range(1, n + 1):
    suma += i

print("La suma es:", suma)