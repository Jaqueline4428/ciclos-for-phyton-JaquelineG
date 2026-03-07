#ejercicio06.py
# Nombre: Jaqueline Gutierrez
# Fecha: 28/02/2026

# Pseudocódigo
# Pedir palabra
# contador = 0
# Para cada letra en palabra
#   Si letra es vocal
#       contador++
# Mostrar contador

palabra = input("Ingrese una palabra: ")
contador = 0

for letra in palabra:
    if letra.lower() in "aeiou":
        contador += 1

print("Cantidad de vocales:", contador)