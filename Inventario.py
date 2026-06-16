from Producto import *
from Estadistica_producto import *
class Inventario:
    def __init__(self):
        self.columnas =["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
        self.productos = []
        self.estadistica_productos = []
    def buscar_producto(self, coordenadas):
        for i_fila in range(len(self.estadistica_prductos)):
            if i_fila +1 == coordenadas[1]:
                for i_columna in range(len(i_fila)):
                    if self.columnas[i_columna] == coordenadas[0]:
                        return self.estadistica_productos[i_fila][i_columna]
        return ""
    def agregar_prducto(self, coordenada):
        nombre = input("Ingrese el nombre del producto que quiere agregar: ")
        precio = input("Ingrese el precio del producto que quiere agregar: ")
        cantidad = input("Ingrese la cantidad del producto que quiere agregar: ")
        producto =  Producto(nombre, precio)
        estadistica = Estadistica_producto(producto, cantidad)
        if len(self.productos) < coordenada[1]:
            self.productos.append([])
        for fila in range(len(self.productos)):
            if fila +1 == coordenada[1]:
                agregado = False 
                for p in range(len(fila)):
                    if self.columnas[p] == coordenada[0]:
                        agregado = True
                        self.productos.insert(p, producto)
                        self.estadistica_productos.insert(p, estadistica)
                if not agregado:
                    self.productos[fila].append(producto)
                    self.estadistica_productos[fila].append(estadistica)
        
                        

                    

