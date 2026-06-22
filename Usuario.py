#Castillo, Yorianny; Cafarelli, Valeria

class Usuario:
    """Representa a un usuario y el dinero que ha gastado"""
    def __init__(self, nombre, dinero_gastado):
        """Guarda los datos básicos del usuario"""
        self.nombre = nombre
        self.dinero_gastado = dinero_gastado
    
    