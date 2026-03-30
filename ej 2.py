#Ejercicio 2 — “Acceso al Campus y Menú Seguro”
usuario_correcto="alumno"
clave_correcta="python123"
maximo_intentos= 3
cantidad_intentos=1

ingresar_ususario=input("Por favor, ingrese su nombre de usuario: ")
ingresar_contraseña= input("Por favor, ingrese su contraseña: ")

while clave_correcta != ingresar_contraseña or usuario_correcto != ingresar_ususario:
    if maximo_intentos <= cantidad_intentos:
        print("Cuenta bloqueada")
        break
    else:
        print(str(cantidad_intentos) + "/3") 
        print("Error: credenciales inválidas.")
        ingresar_ususario=input("Por favor, ingrese su nombre de usuario: ")
        ingresar_contraseña= input("Por favor, ingrese su contraseña: ")
        cantidad_intentos += 1

while ingresar_contraseña==clave_correcta and ingresar_ususario== usuario_correcto:
    print("1) Estado  2)Cambiar clave  3)Mensaje  4)Salir")
    numero_menu= input("Ingrese el número de la opción que desea seleccionar: ")
    if numero_menu.isdigit():
        numero_menu= int(numero_menu)
        if numero_menu==1:
            print("Inscripto")
        elif numero_menu==2:
            print("La nueva clave debe tener al menos 6 dígitos.")
            nueva_clave = input("Ingrese su nueva clave: ")
            repetir_clave = input("Repita su nueva clave: ")
            if len(nueva_clave) >= 6 and nueva_clave == repetir_clave and nueva_clave.isdigit() and repetir_clave.isdigit():
                print("Clave cambiada con éxito.")
            elif nueva_clave != repetir_clave:
                print("Las claves no coinciden.")
                nueva_clave= int(input("Ingrese su nueva clave: "))
                repetir_clave= int(input("Repita su nueva clave: "))
            else:
                print("Error: mínimo 6 caracteres.")
                nueva_clave= input("Ingrese su nueva clave: ")
                repetir_clave= input("Repita su nueva clave: ")
        elif numero_menu==3:
            print("Bienvenido al campus! Esperamos que tengas un excelente día.")
        elif numero_menu==4:
            break
        elif numero_menu > 5:
            print("Error: opción fuera de rango.")
            numero_menu= input("Ingrese el número de la opción que desea seleccionar: ").isdigit()
    else:
        print("Error: ingrese un opción válida.")
        numero_menu= input("Ingrese el número de la opción que desea seleccionar: ").isdigit()


    

