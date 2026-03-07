#ejercicio09.py
# Fecha: 06/03/2026

# Pseudocódigo
# positivos = 0
# negativos = 0
# ceros = 0
# Para 10 veces
#   pedir número
#   si numero > 0 positivos++
#   si numero < 0 negativos++
#   si numero == 0 ceros++
# Mostrar resultados

positivos = 0
negativos = 0
ceros = 0

for i in range(10):
    numero = float(input("Ingrese un número: "))

    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1
    else:
        ceros += 1

print("Positivos:", positivos)
print("Negativos:", negativos)
print("Ceros:", ceros)