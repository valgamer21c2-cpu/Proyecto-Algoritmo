class Modulo_Reporte:
    def __init__(self, inventario):
        self.inventario = inventario
    def mostrar_info(self, ventas, usuarios):
        total_vendidos = 0
        for linea in self.inventario.estadistica_productos:
            for producto in linea:
                print("Producto:",producto.producto.nombre)
                print("Último_restock:",producto.ultimo_restock)
                print("Cantidad_vendidos:",producto.cantidad_vendidos)
                total_vendidos += producto.cantidad_vendidos
        print("Total de productos vendidos:",ventas.total_cantidad_vendidos)
        print("Dinero total cobrado por la máquina:",ventas.dinero_cobrado)
        print("Dinero gastado por los usuarios: ")
        for usuario in usuarios:
            print(usuario.nombre,usuario.dinero_gastado)
        print("Total de usuarios:",ventas.total_usuarios)


        

        
    
        
    

