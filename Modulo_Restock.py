#Castillo, Yorianny; Cafarelli, Valeria

from Validaciones import *
class Modulo_Restock:
    """Maneja el restock y los cambios de productos en la máquina"""
    def __init__(self, inventario):
        """Guarda el inventario que se va a modificar"""
        self.inventario = inventario
    def actualizar(self, coordenada):
        """Actualiza la cantidad disponible de un producto"""
        cantidad_producto = input("Ingrese la nueva cantidad del producto: ")
        cantidad_producto = validar_num(cantidad_producto)
        producto = self.inventario.buscar_producto(coordenada)
        producto.cantidad += int(cantidad_producto)
        producto.ultimo_restock = int(cantidad_producto)
    def cambiar_producto(self, coordenada):
        """Cambia un producto por otro nuevo en una posición del inventario"""
        nuevo_producto = input("Ingrese el nombre del nuevo producto: ")
        nuevo_codigo = input("Ingrese el código del nuevo producto: ")
        cantidad = input("Ingrese la cantidad del nuevo producto: ")
        cantidad = validar_num(cantidad)
        nueva_descripcion = input("Ingrese la despedida del nuevo producto: ")
        est_producto = self.inventario.buscar_producto(coordenada)
        if est_producto: 
            est_producto.producto.nombre = nuevo_producto
            est_producto.producto.codigo = nuevo_codigo
            est_producto.producto.descripcion = nueva_descripcion
            precio = (input("Ingrese el precio del nuevo producto: "))
            precio = validar_float(precio)
            est_producto.producto.precio = precio
            est_producto.cantidad = cantidad
            est_producto.cantidad_vendidos = 0
            est_producto.ultimo_restock = cantidad
        else:
            self.invetario.agregar_producto(nuevo_producto, cantidad)




