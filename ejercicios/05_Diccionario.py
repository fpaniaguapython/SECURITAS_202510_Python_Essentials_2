diccionario = {'edad': 30, 'nombre': 'Fernando', 'ciudad': 'Madrid'}
# No admite claves duplicadas
diccionario['profesion'] = 'Ingeniero' # Agrega un nuevo par clave-valor
diccionario['edad'] = 31 # Modifica el valor asociado a la clave 'edad'
print(diccionario)
print(diccionario['nombre']) # Accede al valor asociado a la clave 'nombre'

print(tuple(diccionario)) # ('edad', 'nombre', 'ciudad', 'profesion')
print(tuple(diccionario.keys())) # ('edad', 'nombre', 'ciudad', 'profesion')
print(tuple(diccionario.values())) # (31, 'Fernando', 'Madrid', 'Ingeniero')

for clave, valor in diccionario.items():
    print(f"{clave}: {valor}")