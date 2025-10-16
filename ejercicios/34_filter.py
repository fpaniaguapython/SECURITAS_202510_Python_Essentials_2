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

# Aplicación de un filter con una función 'normal'
def cuesta_menos_de_30000(automovil : Automovil):
    return automovil.precio < 30_000

candidatos = filter(cuesta_menos_de_30000, automoviles) # Devuelve un objeto de la clase 'filter'

# ¡ATENCIÓN! candidatos no tiene los datos, pero sabe generarlos
candidatos = list(candidatos)
print(candidatos)

# Aplicación de un filter con una función lambda
candidatos_por_plaza = filter(lambda automovil : automovil.numero_plazas > 3, automoviles)
for candidato in candidatos_por_plaza:
    print(candidato)