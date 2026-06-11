#Algoritmo GuardianDeLaPuerta

#Inicio
    #clave ← ""

    #Mientras clave ≠ "SESAMO" Hacer
        #Escribir "Ingrese la palabra clave:"
        #Leer clave

        #Si clave ≠ "SESAMO" Entonces
        #Escribir "Acceso denegado. Intente de nuevo."
        #FinSi
    #FinMientras

    #Escribir "Acceso concedido. Bienvenido."

#Fin
clave = ""

while clave != "SESAMO":
    clave = input("Ingrese la palabra clave: ")

    if clave != "SESAMO":
        print("Acceso denegado. Intente de nuevo.")

print("Acceso concedido. Bienvenido.")