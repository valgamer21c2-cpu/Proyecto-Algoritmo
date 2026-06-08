from Producto import *
from Estadistica_producto import *
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
    def agregar_prducto(self):
        nombre=input("Ingrese nombre del producto")
        precio=input("Ingrese el precio del producto")
        cantidad=input("Ingrese la cantidad")
        producto=Producto(nombre, precio)
        self.productos.append(producto)
        estadistica=Estadistica_producto(producto, cantidad)
        self.estadistica_productos.append(estadistica)
                        

                    

