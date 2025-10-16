'''
Crear una clase Automóvil
- Marca
- Modelo
- Número de plazas
- Precio

Crear 3 instancias de Automóvil y las guardamos en una lista

Ordenación por número de plazas (ascendente) --> Usando función 'normales'
Ordenación por el precio (descendente) --> Usando lambda

'''
class Automovil:
    def __init__(self, marca, modelo, numero_plazas, precio):
        self.marca = marca
        self.modelo = modelo
        self.numero_plazas = numero_plazas
        self.precio = precio

    def __str__(self):
        return f'Marca:{self.marca}. Modelo:{self.modelo}. Número de plazas:{self.numero_plazas}. Precio:{self.precio}'

    def __repr__(self):
        return self.__str__()

automovil_1 = Automovil('Seat', 'Panda', 4, 8_000)
automovil_2 = Automovil('Ford', 'Mustang', 2, 35_000)
automovil_3 = Automovil('BMW', 'Z5', 5, 28_000)

automoviles = [automovil_1, automovil_2, automovil_3]

# Ordenar por plazas con función 'normal'
def cuantificar_por_plazas(automovil : Automovil) -> int:
    return automovil.numero_plazas

automoviles_por_plazas = sorted(automoviles, key=cuantificar_por_plazas)
print(automoviles_por_plazas)

# Ordenar por precio descendente utilizando lambda
automoviles_por_precio = sorted(automoviles, key=lambda automovil : automovil.precio, reverse=True)
print(automoviles_por_precio)