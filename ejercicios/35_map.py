import random

nombres = ['zaragoza', 'madrid', 'cáceres', 'toledo']

class Ciudad:
    def __init__(self, nombre, habitantes):
        self.nombre = nombre
        self.habitantes = habitantes

    def __str__(self):
        return f'Ciudad:{self.nombre}. Habitantes:{self.habitantes}'

    def __repr__(self):
        return self.__str__()

# Transformación 'tradicional'
nombres_mayusculas = []
for nombre in nombres:
    nombres_mayusculas.append(nombre.upper())
print(nombres_mayusculas)

# Función de transformación str a str en mayúsculas con map
def convertir_a_mayusculas(palabra : str):
    return palabra.upper()

# Transformación con map y función 'tradicional'
palabras_convertidas = map(convertir_a_mayusculas, nombres) # Devuelve un objeto map
for palabra in palabras_convertidas:
    print(palabra)

# Transformación con map y función lambda
palabras_convertidas = map(lambda palabra : palabra.upper(), nombres)    
for palabra in palabras_convertidas:
    print("*", palabra)

# Función de transformación str a objeto Ciudad
def convertir_a_objeto_ciudad(nombre_ciudad : str):
    ciudad = Ciudad(nombre_ciudad.capitalize(), random.randint(100_000, 200_000))
    return ciudad

# Transformación con map y función 'tradicional'
ciudades_convertidas = map(convertir_a_objeto_ciudad, nombres)
for ciudad in ciudades_convertidas:
    print(ciudad)

# Transformación con map y función lambda
ciudades_convertidas = map(lambda nombre_ciudad : Ciudad(nombre_ciudad.capitalize(), random.randint(100_000, 200_000)),nombres)
for ciudad in ciudades_convertidas:
    print("*", ciudad)
