#Ejercicio 1- "Caja de Kiosco"
sin_descuentos=0
con_descuentos= 0
ahorro= 0
promedio=0
nombre_cliente= input("Ingrese el nombre del cliente: ").strip()
while not nombre_cliente.isalpha():
    print("Error: El nombre del cliente solo puede contener letras.")
    nombre_cliente= input("Ingrese el nombre del cliente: ").strip()

pedir_cantidad_productos= input("Ingresse la cantidad de productos a comprar: ")
while not pedir_cantidad_productos.isdigit() or int(pedir_cantidad_productos) <= 0:
    print("Error:La cantidad de productos a comprar debe ser un numero mayor a 0")
    pedir_cantidad_productos= input("Ingresse la cantidad de productos a comprar: ")

cantidad_productos=int(pedir_cantidad_productos) 
for i in range(1,cantidad_productos+1):
    precio_producto= input(f"Ingrese el precio del producto {i}: ")
    if not precio_producto.isdigit():
        print("Error: El precio del producto debe ser un numero entero")
        precio_producto= input(f"Ingrese el precio del producto {i}: ")
    else:
        precio_producto= int(precio_producto)
        sin_descuentos+=int(precio_producto)
        
    
    while True:
        descuento_s_n= input("¿El producto tiene descuento? (s/n): ")
        if descuento_s_n=="s" or descuento_s_n=="S":
            descuento_producto= precio_producto*0.10
            precio_descuento= precio_producto-descuento_producto
            con_descuentos+= precio_descuento
            ahorro+=descuento_producto
            break
        elif descuento_s_n=="n" or descuento_s_n=="N":
            con_descuentos+= float(precio_producto)
            break
        else:
            print("Error solo ingrese 's' o 'n'")

    
promedio=con_descuentos/cantidad_productos
promedio=float(promedio)
print(f"Total sin descuentos: {sin_descuentos} ")
print(f"Total con descuentos: {con_descuentos} ")
print(f"Ahorro: {ahorro} ")
print(f"Promedio por producto: {promedio:.2f}")