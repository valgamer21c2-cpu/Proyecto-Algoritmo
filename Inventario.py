class Inventario:
    def __init__(self):
        self.productos = []
        self.estadistica_productos = []
    def buscar_producto(self, coordenadas):
        for fila in range(len( self.prductos)):
            if fila == coordenadas[1]:
                for producto in range(len(fila)):
                    if producto == coordenadas[0]:
                        return fila[producto]
                    
                        

                    

