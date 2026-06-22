#Castillo, Yorianny; Cafarelli, Valeria

from Validaciones import *
from Usuario import *
class Modulo_Venta: 
    """Controla las ventas, los usuarios y el dinero cobrado"""
    def __init__(self, inventario, tarjetas, usuarios):
        """Guarda el inventario, las tarjetas y la lista de usuarios"""
        self.inventario = inventario
        self.tarjetas = tarjetas
        self.usuarios = usuarios
        self.productos_vendidos = 0
        self.dinero_cobrado = 0
        self.total_usuarios = 0
        self.total_cantidad_vendidos = 0
    def realizar_venta(self, coordenada):
        """Hace el proceso de compra de un producto paso a paso"""
        producto = self.inventario.buscar_producto(coordenada)
        if producto == "":
            print("No se econtró el producto")
            return
        precio = producto.producto.precio
        print()
        print(f"El precio del producto es {precio}")
        continuar = input("¿Desea seguir con la compra? Ingrese '1' si la respuesta es SÍ o '2' si la respuesta es NO: ")
        if continuar == "2":
            return 
        tarjeta = input("Ingrese el número de tarjeta: ")
        tarjeta = validar_num(tarjeta)
        #tarjeta = hash(tarjeta) 
        tarjeta = self.buscar_tarjeta(tarjeta)
        if tarjeta == " ":
            return 
        confirmar = input("Para confirmar la compra, por favor escriba el código del producto: ")
        if confirmar == producto.producto.codigo:
            usuario = input("Ingrese su nombre de usuario: ")
            usuario = self.buscar_usuario(usuario)
            tarjeta.saldo -= precio
            producto.cantidad -= 1 
            producto.cantidad_vendidos += 1
            self.total_cantidad_vendidos += 1
            self.productos_vendidos += 1
            self.dinero_cobrado += precio
            usuario.dinero_gastado += precio
            print("...El producto está siendo dispensado...")
            print(producto.producto.descripcion)
        else:
            print("El producto no fue encontrado, se cancela la venta\n")
    def buscar_tarjeta(self, numero_tarjeta):
        """Busca una tarjeta por su número dentro de la lista"""
        for t in self.tarjetas:
            if t.numero_tarjeta == numero_tarjeta:
                return t
        return " "
    def buscar_usuario(self, usuario):
        """Busca un usuario y si no existe lo crea"""
        for u in self.usuarios:
            if u.nombre == usuario:
                return u
        u = Usuario(usuario, 0)
        self.usuarios.append(u)
        self.total_usuarios += 1
        return u