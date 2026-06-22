#Castillo, Yorianny; Cafarelli, Valeria

class Estadistica_producto:
    """Guarda datos simples de ventas y restock de un producto"""
    def __init__ (self, producto, cantidad):
        """Inicializa la cantidad, ventas y último restock del producto"""
        self.cantidad_vendidos = 0
        self.ultimo_restock = cantidad
        self.producto = producto
        self.cantidad = cantidad
