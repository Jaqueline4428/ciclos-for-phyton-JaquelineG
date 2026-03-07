#ejercicio04.py
# Nombre: Jaqueline Gutierrez
# Fecha: 28/02/2026

# Pseudocódigo
# Pedir número
# Para i desde 1 hasta 10
#   resultado = numero * i
#   Mostrar resultado
# Fin Para

numero = int(input("Ingrese un número: "))

for i in range(1, 11):
    print(numero, "x", i, "=", numero * i)