#Algoritmo MenuRestaurante

#Inicio
    #opcion ← 0

    #Mientras opcion ≠ 3 Hacer

        #Escribir "----- MENÚ DEL RESTAURANTE -----"
        #Escribir "1. Pedir comida"
        #Escribir "2. Ver cuenta"
        #Escribir "3. Salir"

        #Leer opcion
        #Si opcion = 1 Entonces
            #Escribir "Has pedido comida."
        #Sino
            #Si opcion = 2 Entonces
            #Escribir "Mostrando la cuenta."
            #Sino
                #Si opcion = 3 Entonces
                    #Escribir "Gracias por visitar el restaurante."
                #Sino
                    #Escribir "Opción inválida."
                #FinSi
            #FinSi
        #FinSi

    #FinMientras

#Fin
opcion = 0

while opcion != 3:
    print("----- MENÚ DEL RESTAURANTE -----")
    print("1. Pedir comida")
    print("2. Ver cuenta")
    print("3. Salir")

    opcion = int(input("Seleccione una opción: "))

    if opcion == 1:
        print("Has pedido comida.")
    elif opcion == 2:
        print("Mostrando la cuenta.")
    elif opcion == 3:
        print("Gracias por visitar el restaurante.")
    else:
        print("Opción inválida, intente nuevamente.")