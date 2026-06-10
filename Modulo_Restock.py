class Modulo_Restock:
    def __init__(self, inventario):
        self.inventario = inventario
    def actualizar(self, coordenada):
        cantidad_producto = input("Ingrese la nueva cantidad de producto")
        producto = self.inventario.buscar_producto(coordenada)
        producto.cantidad += cantidad_producto
        producto.ultimo_restock = cantidad_producto
    def cambiar_producto(self, coordenada):
        nuevo_producto = input("Ingrese el codigo del nuevo producto")
        cantidad = input("Ingrese la cantidad del nuevo producto")
        producto = self.inventario.buscar_producto(coordenada)
        if producto : 
            producto. nombre = nuevo_producto
            producto.cantidad = cantidad
        else :
            self.invetario.agregar_producto (nuevo_producto, cantidad)



