class Modulo_Catalogo: 
    def __init__(self, inventario):
        self.inventario = inventario
    def mostrar_catalogo(self):
        print("Catálogo de productos: ")
        for fila in self.inventario.productos:
            linea = " "
            for p in fila: 
                linea += p.nombre + " "
            print(linea)

