#Castillo, Yorianny; Cafarelli, Valeria

from Modulo_Catalogo import Modulo_Catalogo
from Modulo_Restock import Modulo_Restock
from Usuario import Usuario
from Modulo_Reporte import Modulo_Reporte
from Modulo_Venta import Modulo_Venta 
from Inventario import Inventario
from Api import *
inventario = leer_archivo()
inventario = leer_api_productos(inventario)
lista_tarjetas = leer_api_tarjeta()
usuarios = []
ventas = Modulo_Venta(inventario, lista_tarjetas, usuarios)
restock = Modulo_Restock(inventario) 
catalogo = Modulo_Catalogo(inventario)
reporte = Modulo_Reporte(inventario)

while True: 
    print()
    catalogo.mostrar_catalogo()
    print()
    input_usuario = input("Ingrese el código del prducto para ver el precio\nIntroduce RS para inciar el restock\nIntroduce RP para generar un reporte\nIngrese S para salir\n---> ")
    if len(input_usuario) == 2 and input_usuario[0].isalpha() and input_usuario[1].isnumeric():
        ventas.realizar_venta(input_usuario)
    elif input_usuario == "RS":
        opcion = input("Ingrese 1 para actualizar existencia del inventario\nIngrese 2 para cambiar producto\nIngrese 3 para salir\n --->")
        if opcion == "3":
            continue
        coordenada = input("Ingrese la coordenada del producto (ejemplo: A1, B2, etc.)\n --->")
        if opcion == "1":
            restock.actualizar(coordenada)
        elif opcion == "2":
            restock.cambiar_producto(coordenada)
    elif input_usuario == "RP":
        reporte.mostrar_info(ventas, usuarios)
    elif input_usuario == "S":
        print("¡Gracias por su compra!")
        break
    guardar_archivo(inventario)
    