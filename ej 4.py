#Ejercicio 4 — “Escape Room: La Bóveda”
energia = 100
max_energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""
contador= 0
ultima_opcion= None
max_intentos_cerradura= 3
bloqueo_alarma= 0

nombre_agente = input("Ingrese el nombre del agente: ")
while not nombre_agente.isalpha():
    print("El nombre del agente solo puede contener letras. Intente de nuevo.")
    nombre_agente= input("Ingrese el nombre del agente: ")

while energia> 0 and tiempo>0 and cerraduras_abiertas<3 and bloqueo_alarma!=1:
    opciones_menú= input("Seleccione una opción: \n1. Forzar cerradura (costo: -20 energía, -2 tiempo)\n2. Hackear panel (costo: -10 energía, -3 tiempo)\n3. Descansar (costo: +15 energía (máx 100), -1 tiempo; si alarma ON: -10 energía extra): ")
    
    while not opciones_menú.isdigit():
        print("Opcion invalida. Seleccione un numero del 1 al 3.")
        opciones_menú = input("Seleccione una opción: \n1. Forzar cerradura (costo: -20 energía, -2 tiempo)\n2. Hackear panel (costo: -10 energía, -3 tiempo)\n3. Descansar (costo: +15 energía (máx 100), -1 tiempo; si alarma ON: -10 energía extra): ")

    opciones_menú= int(opciones_menú)
    
    if opciones_menú == 1:
        if opciones_menú==ultima_opcion:
            contador+=1
        else:
            ultima_opcion=opciones_menú
            contador=1

        if contador>2:
            alarma=True        
            print("Demasiados intentos! La cerrradura se trabó")
            
        if energia>=40:
                energia-=20
                tiempo-=2
                print("Intentaste forzar la cerradura.")
        if energia < 40:
            print("Riesgo de alarma")
                
        numero_cerradura_forzada=input("Elija un numero del 1 al 3: ")
        while not numero_cerradura_forzada.isdigit():
            print("Opcion invalida. Seleccione una opcion del 1 al 3.")
            numero_cerradura_forzada=input("Elija un numero del 1 al 3: ")
        numero_cerradura_forzada= int(numero_cerradura_forzada)
                
        if numero_cerradura_forzada == 3:
                alarma = True
                print("¡Alarma activada!")
        else: 
            cerraduras_abiertas += 1
            print(f"Cerradura forzada con éxito! Cerraduras abiertas: {cerraduras_abiertas}")
        energia-=20
        tiempo-=2

    elif opciones_menú == 2:
        energia-=10
        tiempo-=3
        for i in range(4):
           codigo_parcial+= "A"
           print("Progreso hackeo: " + codigo_parcial)
        if len(codigo_parcial) >= 8:
               cerraduras_abiertas += 1
               print("Hackeo exitoso! Cerradura abierta.")
    else: 
        tiempo-=1
        if energia < max_energia:
            energia+=15
        if alarma == True:
            energia-=10
        print("Descansaste y recuperaste energía")
if cerraduras_abiertas == 3:
     print("VICTORIA")
elif alarma == True and tiempo<= 3 and cerraduras_abiertas<3:
    bloqueo_alarma= 1
    print("DERROTA (bloqueaste el sistema)")
elif energia <= 0 or tiempo <= 0 :
    print("DERROTA (te quedaste sin recursos)")
    print("VICTORIA")