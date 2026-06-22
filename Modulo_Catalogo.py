#Castillo, Yorianny; Cafarelli, Valeria

class Modulo_Catalogo: 
    """Muestra el catálogo de productos disponibles en la máquina"""
    def __init__(self, inventario):
        """Guarda el inventario que se va a mostrar"""
        self.inventario = inventario
    def mostrar_catalogo(self):
        """Imprime los códigos de los productos disponibles"""
        print("Catálogo de productos: ")
        for fila in self.inventario.productos:
            linea = " "
            for p in fila: 
                linea += p.codigo + " "
            print(linea)

