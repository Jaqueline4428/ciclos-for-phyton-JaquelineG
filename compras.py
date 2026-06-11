with open("C:\\Users\\jaque\\OneDrive\\Escritorio\\programacion 2026\\compras.txt", "w") as archivo:
    while True:
        nombre = input("Ingrese nombre del producto (o 'fin' para terminar): ")
        if nombre.lower() == "fin":
            break
        
        cantidad = int(input("Ingrese cantidad: "))
        precio = float(input("Ingrese precio unitario: "))
        
        archivo.write(f"{nombre},{cantidad},{precio}\n")

        subtotal = 0
productos = []

with open("C:\\Users\\jaque\\OneDrive\\Escritorio\\programacion 2026\\compras.txt", "r")as archivo:
    for linea in archivo:
        nombre, cantidad, precio = linea.strip().split(",")
        cantidad = int(cantidad)
        precio = float(precio)
        
        total_producto = cantidad * precio
        subtotal += total_producto
        
        productos.append((nombre, cantidad, precio, total_producto))

if subtotal > 100:
    descuento = subtotal * 0.10
elif subtotal > 50:
    descuento = subtotal * 0.05
else:
    descuento = 0

total_pagar = subtotal - descuento

print("\n--- LISTADO DE PRODUCTOS ---")
for p in productos:
    print(f"{p[0]} | Cantidad: {p[1]} | Precio: Q{p[2]} | Total: Q{p[3]}")

print("\nSubtotal:", subtotal)
print("Descuento:", descuento)
print("Total a pagar:", total_pagar)