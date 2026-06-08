class Modulo_Catalogo: 
    def __init__(self, inventario):
        self.inventario = inventario
    def mostrar_catalogo(self):
        print("Catálogo de productos:")
        for producto in self.productos:
            linea = ""
            for p in producto: 
                linea += p.nombre + " "
            print(linea)
        producto=[[1,2,3],[4,5,6],[7,8,9]]
