from Producto import *
from Estadistica_producto import *
class Inventario:
    def __init__(self):
        self.columnas =["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
        self.productos = []
        self.estadistica_productos = []
    def buscar_producto(self, coordenadas):
        for fila in range(len( self.prductos)):
            if fila +1 == coordenadas[1]:
                for producto in range(len(fila)):
                    if self.columnas[producto] == coordenadas[0]:
                        return fila[producto]
    def agregar_prducto(self, coordenada):
        nombre=input("Ingrese nombre del producto")
        precio=input("Ingrese el precio del producto")
        cantidad=input("Ingrese la cantidad")
        producto=Producto(nombre, precio)
        estadistica=Estadistica_producto(producto, cantidad)
        for fila in range(len(self.productos)):
            if fila +1 == coordenada [1]:
                for p in range(len(fila)):
                    if self.columnas[p]== coordenada[0]:
                        self.productos.insert(p, producto)
                        self.estadistica_productos.insert(p, estadistica)

        
                        

                    

