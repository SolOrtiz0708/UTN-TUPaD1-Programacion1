#Ejercicio 5 — “Escape Room:"La Arena del Gladiador"
vida_gladiador= 100
vida_enemigo= 100
pociones_vida= 3
daño_base_gladiador= 15
daño_base_enemigo=12
turno_gladiador= True

nombre_gladiador= input("Ingrese el nombre de su gladiador: ")
while not nombre_gladiador.isalpha():
    print("Error. Solo se permiten letras.")
    nombre_gladiador= input("Ingrese el nombre de su gladiador: ")
while vida_gladiador > 0 and vida_enemigo > 0:
    if turno_gladiador==True:
        print(f"Vida de {nombre_gladiador}: {vida_gladiador}\nVida del enemigo: {vida_enemigo}\nPociones de vida: {pociones_vida}")
        opcion_menú= input("Seleccione una opción: \n1. Atacaque Pesado\n2.Ráfaga veloz\n3.Curar\n")
        while not opcion_menú.isdigit():
            print("Error. Sólo puede ingresar números.")
            opcion_menú= input("Seleccione una opción: \n1. Atacaque Pesado\n2.Ráfaga veloz\n3.Curar: ")
        opcion_menú=int (opcion_menú)
        while opcion_menú < 1 or opcion_menú > 3:
            print("Error. Debe elegir una opción del 1 al 3.")
            opcion_menú= input("Seleccione una opción: \n1. Atacaque Pesado\n2.Ráfaga veloz\n3.Curar: ")
        opcion_menú=int (opcion_menú)
        if opcion_menú == 1:
            if vida_enemigo < 20:
                golpe_crítico= daño_base_gladiador * 1.5
                golpe_crítico= float(golpe_crítico)
                vida_enemigo-= golpe_crítico
                vida_enemigo= float(vida_enemigo)
                print(f"¡Atacaste al enemigo por {golpe_crítico} puntos de daño!")
            else:
                vida_enemigo-= daño_base_gladiador
                print(f"¡Atacaste al enemigo por {daño_base_gladiador} puntos de daño!")
        elif opcion_menú == 2:
            for i in range(3):
                vida_enemigo-= 5
            print("> Golpe conectado por 5 de daño.")
        else:
            if pociones_vida > 0:
                vida_gladiador+= 30
                pociones_vida-=1
            else:
                print("¡No quedan pociones!")
        turno_gladiador= False
    else:
        vida_gladiador -= daño_base_enemigo
        print("¡El enemigo te atacó por 12 puntos de daño!")
        turno_gladiador= True
if vida_gladiador > 0:
    print(f"¡VICTORIA! {nombre_gladiador} ha ganado la batalla.")
else:
    print("DERROTA.Has caído en combate.")

