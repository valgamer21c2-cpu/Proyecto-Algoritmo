def validar_num(num):
    while not num.isnumeric():
        num = input("Ingrese un número válido: ")
    return int(num)

def validar_float(num):
    while not num.isnumeric():
        num = input("Ingrese un número válido: ")
    return float(num)

def validar_coordenada(coordenada):
    while not coordenada[0].isalpha() or not coordenada[1].isnumeric() or len(coordenada) != 2:
        coordenada = input("Ingrese una coordenada válida: ")
    return coordenada