#ciclo-while-1.py
numero= int(input("ingrese un numero(0 para terminar):"))

contador=0

while numero!=0:
    contador = contador +1 
    numero = int(input("Ingrese un numero(0 para terminar):"))
    print("Cantidad de numeros ingresados", contador)