class Tarjeta:
    def __init__(self, numero_tarjeta, fecha_vencimiento, cvc, saldo, banco):
        self.numero_tarjeta = numero_tarjeta
        self.fecha_vencimiento = fecha_vencimiento
        self.cvc = cvc
        self.saldo = saldo
        self.bando = banco
    def validar(self):
        pass
    def cifrar(self):
        pass
    def descifrar(self, hash):
        pass