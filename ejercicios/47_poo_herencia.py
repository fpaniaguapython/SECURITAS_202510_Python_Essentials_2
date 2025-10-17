class Vehiculo:
    def __init__(self, marca, modelo, capacidad):
        self.marca = marca
        self.modelo = modelo
        self.capacidad = capacidad

    def saludar(self):
        print('Soy Vehiculo')

class Automovil(Vehiculo):
    def __init__(self, marca, modelo, capacidad, numero_ruedas):
        super().__init__(marca, modelo, capacidad) # Ejecutar el __init__ de Vehiculo
        self.numero_ruedas = numero_ruedas
    
    def saludar(self):
        print('Soy Automovil')


mi_automovil = Automovil('Seat', 'Panda', 4, 4)
print(isinstance(mi_automovil, Automovil)) # True
print(isinstance(mi_automovil, Vehiculo)) # True --> Polimorfismo
mi_automovil.saludar() # Soy Automovil


