class Modulo_Reporte:
    def __init__(self, inventario):
        self.inventario = inventario
    def mostrar_info(self, ventas, restock, productos, usuarios):
        total_vendidos = 0
        for producto in productos:
            print("producto: "+ producto.nombre)
            print("-ultimo_restock: "+ producto.ultimo_restock)
            print("cantidad_vendidos: "+ producto.cantidad_vendidos)
            total_vendidos += producto.cantidad_vendidos
        print("total_vendidos:"+ producto.cantidad_vendidos)
        print("dinero cobrado total cobrado por la maquina: "+ ventas.dinero_cobrado)
        for usuario in usuarios:
            print("usuario:"+ usuario.dinero_gastado)
        print("total usuarios: "+ ventas.total_usuarios)


        

        
    
        
    

