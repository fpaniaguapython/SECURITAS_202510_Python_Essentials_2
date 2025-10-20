class Vehiculo:
    def __init__(self, velocidad):
        self.velocidad = velocidad
    def arrancar_motor(self):
        print('Arrancando motor (Vehiculo)...')
    def parar_motor(self):
        print('Parando motor (Vehiculo)...')

class Barco(Vehiculo):
    def __init__(self, velocidad, eslora, manga):
        self.eslora = eslora
        self.manga = manga
    def parar_motor(self):
        print('Parando motor (Barco)...')
    def navegar(self):
        print('Navegando (Barco)...')

class Automovil(Vehiculo):
    def __init__(self, velocidad, numero_puertas):
        self.numero_puertas = numero_puertas
    def parar_motor(self):
        print('Parando motor (Automovil)...')
    def circular(self):
        print('Circulando (Automovil)...')


class Anfibio(Barco, Automovil):
    def __init__(self, velocidad, eslora, manga, numero_puertas):
        pass
    def parar_motor(self):
        print('Parando motor (Anfibio)...')


vehiculo_anfibio = Anfibio(velocidad=100, eslora=10, manga=3, numero_puertas=4)
vehiculo_anfibio.arrancar_motor()
vehiculo_anfibio.navegar()
vehiculo_anfibio.circular()
vehiculo_anfibio.parar_motor()

        