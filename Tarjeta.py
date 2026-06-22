#Castillo, Yorianny; Cafarelli, Valeria

class Tarjeta:
    """Representa una tarjeta con número y saldo disponible"""
    def __init__(self, numero_tarjeta, saldo):
        """Guarda el número de tarjeta y su saldo"""
        self.numero_tarjeta = numero_tarjeta
        self.saldo = saldo