from Modulo_Catalogo import Modulo_Catalogo
from Modulo_Restock import Modulo_Restock
from Usuario import Usuario
from Modulo_Reporte import Modulo_Reporte
from Modulo_Venta import Modulo_Venta 
from Inventario import Inventario
inventario = Inventario()
usuarios = []
ventas = Modulo_Venta(inventario)
restock = Modulo_Restock(inventario) 
catalogo = Modulo_Catalogo(inventario)
reporte = Modulo_Reporte(inventario)
while True: 
    input_usuario = input ("Ingrese codigo del prducto para ver el precio\nDejar en blanco para comenzar la venta\nIntroduce RS para inciar el restock\nIntroduce RP para generar un reporte\nIngrese S para salir\n---> ")
    if input_usuario == " ":
        usuario = input("Ingrese su nombre\n --->")
        tarjeta = input("Ingrese su numero de tarjeta\n --->")
        usuarios.append(Usuario(usuario, 0, tarjeta))
        ventas.realizar_venta()
    elif input_usuario == "RS":
        opcion = input("Ingrese 1 para actualizar existencia del inventario\nIngrese 2 para cambiar producto\nIngrese 3 para salir\n --->")
        coordenada = input("Ingrese la coordenada del producto a actualizar (ejemplo: A1, B2, etc.)\n --->")
        if opcion == "1":
            restock.actualizar(coordenada)
        elif opcion == "2":
            restock.cambiar_producto(coordenada)
        elif opcion == "3":
            continue
    elif input_usuario == "RP":
        reporte.mostrar_info(ventas, restock, inventario, usuarios)
    elif input_usuario == "S":
        break
    else: 
        ventas.buscar_precio(input_usuario)
