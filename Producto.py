#Castillo, Yorianny; Cafarelli, Valeria

class Producto: 
    """Guarda los datos iniciales del producto"""
    def __init__(self, nombre, codigo, precio, descripcion):
        """Representa un producto con su nombre, código, precio y descripción"""
        self.nombre = nombre
        self.codigo = codigo
        self.precio = precio
        self.descripcion = descripcion
