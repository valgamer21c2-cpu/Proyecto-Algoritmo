from Modulo_Catalogo import Modulo_Catalogo
from Modulo_Restock import Modulo_Restock
from Usuario import Usuario
from Modulo_Reporte import Modulo_Reporte
from Modulo_Venta import Modulo_Venta 
from Inventario import Inventario
from Api import *
inventario = Inventario()
inventario.productos,lista_tarjetas = leer_datos ()
inventario.iniciar_inventario ()
usuarios = []
ventas = Modulo_Venta(inventario,lista_tarjetas,usuarios)
restock = Modulo_Restock(inventario) 
catalogo = Modulo_Catalogo(inventario)
reporte = Modulo_Reporte(inventario)
#archivo txt
while True: 
    catalogo.mostrar_catalogo()
    input_usuario = input("Ingrese el código del prducto para ver el precio\nIntroduce RS para inciar el restock\nIntroduce RP para generar un reporte\nIngrese S para salir\n---> ")
    if input_usuario[0].isalpha() and input_usuario[1].isnumeric() and len(input_usuario) <= 3:
        ventas.realizar_venta(input_usuario)
    elif input_usuario == "RS":
        opcion = input("Ingrese 1 para actualizar existencia del inventario\nIngrese 2 para cambiar producto\nIngrese 3 para salir\n --->")
        coordenada = input("Ingrese la coordenada del producto (ejemplo: A1, B2, etc.)\n --->")
        if opcion == "1":
            restock.actualizar(coordenada)
        elif opcion == "2":
            restock.cambiar_producto(coordenada)
        elif opcion == "3":
            continue
    elif input_usuario == "RP":
        reporte.mostrar_info(ventas, usuarios)
    elif input_usuario == "S":
        print("¡Gracias por su compra!")
        break
    