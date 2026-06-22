#Castillo, Yorianny; Cafarelli, Valeria

import pickle
import requests
from Producto import Producto
from Tarjeta import Tarjeta
def leer_api_tarjeta():
    """Lee las tarjetas desde la API y las guarda en una lista"""

    url_clientes = "https://raw.githubusercontent.com/FernandoSapient/BPTSP05_2526-3/main/clientes.json"

    r1 = requests.get(url_clientes)

    if r1.status_code != requests.codes.ok:
        r1.raise_for_status()

    clientes = r1.json()

    lista_tarjetas = []
    
    for cliente in clientes:
        id = cliente["id"]
        saldo = cliente["saldo"]
        cliente = Tarjeta(id, saldo)
        lista_tarjetas.append(cliente)
    return lista_tarjetas

def leer_api_productos(inventario):
    """Lee productos desde la API y actualiza los precios del inventario"""

    url_productos = "https://raw.githubusercontent.com/FernandoSapient/BPTSP05_2526-3//main/productos.json"

    r2 = requests.get(url_productos)

    if r2.status_code != requests.codes.ok:
        r2.raise_for_status()

    productos = r2.json()

    lista_productos = [[]]
    contador = 1
    indice = 0

    """
    for producto in productos:
        codigo = producto["cod"]
        p = producto["prod"]
        precio = producto["precio"]
        despedida = producto["despedida"]
        producto = Producto(p, codigo, precio, despedida)
        if contador <=5 :
             lista_productos[indice].append(producto)
             contador +=1
        else :
            indice += 1
            if indice > 4:
                break
            lista_productos.append([])
            lista_productos[indice].append(producto)
            contador = 2
    """

    for producto in productos:
        for fila in inventario.productos:
            encontrado = False
            for p in fila:
                if p.codigo == producto["cod"]:
                    if p.precio != producto["precio"]:
                        p.precio = producto["precio"]
                    encontrado = True
                    break
            if encontrado:
                break
                
    return inventario

"""
def leer_archivo():
    archivo = open("archivo.txt", 'r')
    datos = archivo.read()
    archivo.close()
    return datos
def guardar_archivo(estadistica_producto):
    archivo = open("archivo.txt", "w")
    archivo.write(estadistica_producto)
    archivo.close()
"""

def guardar_archivo(estadistica_producto):
    """Guarda el inventario en un archivo para no perder los datos"""
    with open("archivo.pkl", "wb") as archivo:
        pickle.dump(estadistica_producto, archivo)

def leer_archivo():
    """Lee el archivo guardado y devuelve los datos del inventario"""
    try:
        with open("archivo.pkl", "rb") as archivo:
            datos = pickle.load(archivo)
        return datos
    except FileNotFoundError:
        return None