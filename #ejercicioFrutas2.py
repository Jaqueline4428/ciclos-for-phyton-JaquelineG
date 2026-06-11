#ejercicioFrutas2
frutas = []
numeroFruta = range(1,6)
i = 0
for i in numeroFruta:
    fruta = input(f"Ingrese la fruta no.{i}: ")
    frutas.append(fruta)
 
print("Las frutas ingresadas fueron:", frutas)
print("la primera fruta de la lista es: ", frutas[0])
print("La última fruta de la lista es: ",frutas[4])