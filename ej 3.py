#Ejercicio 3 (Alta) — “Agenda de Turnos con Nombres (sin listas)”
opcion_menu= " "
lunes1=" "
lunes2=" "
lunes3=" "
lunes4=" "
martes1=" "
martes2=" "
martes3=" "
1=="Lunes"
2=="Martes"
cupos_lunes= 4
lugar_lunes=0
cupos_martes= 3
lugar_martes=0
agenda_lunes= 0
agenda_martes= 0
nombre_paciente_reserva=" "



nombre_operador= input("Ingrese el nombre del operador: ")
while not nombre_operador.isalpha():
    print("Error: El nombre del operador solo tiene que tener letras.")
    nombre_operador= input("Ingrese el nombre del operador: ")
while opcion_menu != 5:
    print("Menú: \n 1. Reservar turno \n 2. Cancelar turno (por nombre) \n 3. Ver agenda del día\n 4. Ver resumen general\n 5. Cerrar sistema")
    opcion_menu= input("Ingrese el número de la opción que desea seleccionar: ")
    if opcion_menu.isdigit():
        opcion_menu= int(opcion_menu)
        if opcion_menu==1:
            print("Reservar:")
            día_reserva= input("Ingrese 1/ 2 para elegir que díareservar el turno (1=Lunes, 2=Martes):  ")
            while not día_reserva.isdigit() and (día_reserva!= "1" and día_reserva!= "2"):
                print("Error: Ingrese 1 o 2 para elegir el día del turno.")
                día_reserva= input("Ingrese 1/ 2 para elegir que día reservar el turno (1=Lunes, 2=Martes):  ")
            nombre_paciente_reserva= input ("Ingrese el nombre del paciente: ")

            while not nombre_paciente_reserva.isalpha():
                print("Error: El nombre del paciente solo tiene que tener letras.")
                nombre_paciente_reserva= input ("Ingrese el nombre del paciente: ")
            

            if día_reserva== "1":
                if nombre_paciente_reserva == lunes1 or nombre_paciente_reserva == lunes2 or nombre_paciente_reserva == lunes3 or nombre_paciente_reserva == lunes4:
                   print("El paciente ya tiene un turno reservado para el día Lunes.") 
                else:
                    if lunes1==" ":
                        lunes1= nombre_paciente_reserva
                        print("Turno reservado para el día Lunes1.")
                    elif lunes2==" ":
                        lunes2= nombre_paciente_reserva
                        print("Turno reservado para el día Lunes2.")
                    elif lunes3==" ":
                        lunes3= nombre_paciente_reserva
                        print("Turno reservado para el día Lunes3.")
                    else:
                        lunes4= nombre_paciente_reserva
                        print("Turno reservado para el día Lunes4.")
                    lugar_lunes +=1
                    cupos_lunes-=1
                    agenda_lunes= nombre_paciente_reserva + (f"(Turno: {lugar_lunes})")
            else:
                if martes1==nombre_paciente_reserva:
                    print("El paciente ya tiene un turno reservado para el día Martes.")
                else:
                    if martes1==" ":
                        print("Turno reservado para el día Martes1.")
                    elif martes2==" ":
                        martes2= nombre_paciente_reserva
                        print("Turno reservado para el día Martes2.")
                    else:
                        martes3= nombre_paciente_reserva
                        print("Turno reservado para el día Martes3.")
                    lugar_martes +=1
                    cupos_martes-=1
                    agenda_martes= nombre_paciente_reserva + (f"(Turno: {lugar_martes})")
            if cupos_lunes==0 and cupos_martes==0:
                print("No hay más turnos disponibles para el día seleccionado.")
            
            
        elif opcion_menu==2:
            print("Cancelar:")
            día_cancelar= input("Ingrese 1/ 2 para elegir que día cancelar el turno (1=Lunes, 2=Martes):  ")
            while not día_cancelar.isdigit() and (día_cancelar!= "1" and día_cancelar!= "2"):
                print("Error: Ingrese 1 o 2 para elegir el día del turno a cancelar.")
                día_cancelar= input("Ingrese 1/ 2 para elegir que día cancelar el turno (1=Lunes, 2=Martes):  ")
            nombre_paciente_cancelar=input("Ingrese el nombre del paciente para cancelar su turno: ")
            while not nombre_paciente_cancelar.isalpha():
                print("Error: El nombre del paciente solo tiene que tener letras.")
                nombre_paciente_cancelar=input("Ingrese el nombre del paciente para cancelar su turno: ")
            if día_cancelar== "1":
                if lunes1==nombre_paciente_cancelar:
                    lunes1= ""
                    print("Turno cancelado del día Lunes1.")
                elif lunes2==nombre_paciente_cancelar:
                    lunes2= ""
                    print("Turno cancelado del día Lunes2.")
                elif lunes3==nombre_paciente_cancelar:
                    lunes3= ""
                    print("Turno cancelado del día Lunes3.")
                else:
                    lunes4= ""
                    print("Turno cancelado del día Lunes4.")
                if (nombre_paciente_cancelar== nombre_paciente_reserva) and (lugar_lunes > 0):
                    cupos_lunes +=1
                    lugar_lunes-= 1
                else:
                    print("No se encontró ningun turno el Lunes para cancelar.")
            else:
                if martes1==nombre_paciente_cancelar:
                    martes1= ""
                    print("El paciente ha cancelado su turno del día Martes10.")

                elif martes2==nombre_paciente_cancelar:
                    martes2= ""
                    print("El paciente ha cancelado su turno del día Martes2.")
                
                elif martes3==nombre_paciente_cancelar:
                        martes3
                        print("El paciente ha cancelado su turno del día Martes3.")
                else:
                     print("Error: No se encontró el turno para cancelar.")
                if (nombre_paciente_cancelar== nombre_paciente_reserva) and (lugar_martes > 0):
                    cupos_martes +=1
                    lugar_martes-= 1
                else:
                    print("No se encontró el ningún turno el Martes para cancelar.")

        elif opcion_menu==3:
            print("Ver agenda del día:")
            print("Lunes: " + str(agenda_lunes))
            print("Martes: " + str(agenda_martes))
        elif opcion_menu==4:
            print("Resumen general")
            print(f"Nombre del paciente: {nombre_paciente_reserva} \n Turnos ocupados: {1+2} \n Turnos disponibles:\n Lunes: {cupos_lunes} \n Martes: {cupos_martes} ")
            if agenda_lunes > agenda_martes:
                print(f"Día con más turnos: Lunes") 
            elif agenda_martes > agenda_lunes:
                print(f"Día con más turnos: Martes")
            else:
                print("Ambos días tienen la misma cantidad de turnos.")

        elif opcion_menu==5:
            break
        else:
            print("Error: ingrese un opción válida.")
            opcion_menu= input("Ingrese el número de la opción que desea seleccionar: ")
    
