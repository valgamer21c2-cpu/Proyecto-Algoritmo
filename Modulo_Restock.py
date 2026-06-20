class Modulo_Restock:
    def __init__(self, inventario):
        self.inventario = inventario
    def actualizar(self, coordenada):
        cantidad_producto = input("Ingrese la nueva cantidad de producto: ")
        producto = self.inventario.buscar_producto(coordenada)
        producto.cantidad += int(cantidad_producto)
        producto.ultimo_restock = int(cantidad_producto)
    def cambiar_producto(self, coordenada):
        nuevo_producto = input("Ingrese el codigo del nuevo producto: ")
        cantidad = input("Ingrese la cantidad del nuevo producto: ")
        est_producto = self.inventario.buscar_producto(coordenada)
        if est_producto : 
            est_producto.producto.nombre = nuevo_producto
            precio = float(input("Ingrese el precio del nuevo producto: "))
            est_producto.producto.precio = precio
            est_producto.cantidad = cantidad
            est_producto.cantidad_vendidos = 0
            est_producto.ultimo_restock = cantidad
        else :
            self.invetario.agregar_producto(nuevo_producto, cantidad)




