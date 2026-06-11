#Algoritmo AlcanciaAhorros

#Inicio
    #total ← 0

    #Mientras total < 500 Hacer
        #Escribir "Ingrese cuánto dinero va a ahorrar:"
        #Leer dinero

        #total ← total + dinero

        #Escribir "Total ahorrado: ", total
    #FinMientras

    #Escribir "¡Felicidades! Ya tienes suficiente dinero para la consola."

#Fin
total = 0

while total < 500:
    dinero = float(input("Ingrese cuánto dinero va a ahorrar hoy: Q"))
    
    total = total + dinero
    
    print("Total ahorrado:", total)

print("¡Felicidades! Ya puedes comprar la consola.")