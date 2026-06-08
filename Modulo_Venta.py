class Modulo_Venta: 
    def __init__(self, inventario):
        self.inventario = inventario
        self.productos_vendidos = 0
        self.dinero_cobrado = 0
        self.total_usuarios = 0
    def buscar_precio(self, precio):
        pass
    def realizar_venta(self):
        coordenada=input("Ingrese la coordenada del producto: ") 
        producto =self.inventario.buscar_producto(coordenada)
        precio=self.buscar_precio(coordenada)
        targeta=input("Ingrese número de targeta")
        if targeta == " ":
            return 
        targeta=hash(targeta)
        confirmar=input("Para confirmar la compra profavor escriba nombre del producto")
        if confirmar == producto.nombre:
            targeta.saldo -= precio
            producto.cantidad -=1 
            producto.cantidad_vendidos +=1
            self.productos_vendidos +=1
            self.dinero_cobrado +=precio
            print("El producto está siendo dispensado")
        
    def buscar_tarjeta(self, numero_tarjeta):
        pass


    