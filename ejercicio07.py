#ejercicio07.py
# Fecha: 6/03/2026

# Pseudocódigo
# suma = 0
# Para i desde 1 hasta 5
#   pedir nota
#   suma = suma + nota
# promedio = suma / 5
# Mostrar promedio

suma = 0

for i in range(5):
    nota = float(input("Ingrese una nota: "))
    suma += nota

promedio = suma / 5

print("El promedio es:", promedio)