#Castillo, Yorianny; Cafarelli, Valeria

def validar_num(num):
    """Verifica que el dato ingresado sea un número entero válido"""
    while not num.isnumeric():
        num = input("Ingrese un número válido: ")
    return int(num)

def validar_float(num):
    """Verifica que el dato ingresado sea un número válido para precio"""
    while not num.isnumeric():
        num = input("Ingrese un número válido: ")
    return float(num)

def validar_coordenada(coordenada):
    """Verifica que la coordenada tenga letra y número correctamente"""
    while not coordenada[0].isalpha() or not coordenada[1].isnumeric() or len(coordenada) != 2:
        coordenada = input("Ingrese una coordenada válida: ")
    return coordenada