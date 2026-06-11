#Algoritmo Ascensor

#Inicio
   #piso 1

  #Mientras piso <= 5 Hacer
        #faltan ← 5 - piso
        
        #Escribir "Ascensor en piso: ", piso
        #Escribir "Faltan ", faltan, " pisos para llegar al 5"
        
        #piso ← piso + 1
    #FinMientras

#Fin
piso = 1

while piso <= 5:
    faltan = 5 - piso
    
    print("Ascensor en piso:", piso)
    print("Faltan", faltan, "pisos para llegar al 5")
    
    piso += 1
    