import requests
from Producto import Producto
from Tarjeta import Tarjeta
def leer_datos():
    url_clientes = "https://raw.githubusercontent.com/FernandoSapient/BPTSP05_2526-3/main/clientes.json"

    r1 = requests.get(url_clientes)

    if r1.status_code != requests.codes.ok:
        r1.raise_for_status()

    clientes = r1.json()

    url_productos = "https://raw.githubusercontent.com/FernandoSapient/BPTSP05_2526-3//main/productos.json"

    r2 = requests.get(url_productos)

    if r2.status_code != requests.codes.ok:
        r2.raise_for_status()

    productos = r2.json()

    lista_productos = [[]]
    lista_tarjetas = []
    contador = 1
    indice = 0

    for producto in productos:
        codigo = producto["cod"]
        p = producto["prod"]
        precio = producto["precio"]
        despedida = producto["despedida"]
        producto = Producto(p, codigo, precio, despedida)
        if contador <=3 :
             lista_productos[indice].append(producto)
             contador +=1
        else :
            lista_productos.append ([])
            indice += 1
            lista_productos[indice].append(producto)
            contador =2


    for cliente in clientes:
        id = cliente["id"]
        saldo = cliente["saldo"]
        cliente = Tarjeta(id, saldo)
        lista_tarjetas.append(cliente)
    print(lista_tarjetas)
    return lista_productos,lista_tarjetas