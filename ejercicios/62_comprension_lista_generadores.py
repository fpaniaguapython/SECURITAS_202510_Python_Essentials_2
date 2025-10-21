def transformacion(palabra : str):
    palabra_transformada = palabra.replace('a','@').replace('A','@') # Method chaining
    return palabra_transformada

palabras = ['patata', 'América', 'agua', 'vacaciones']

# Sin comprensión de listas

palabras_transformadas = list()
for palabra in palabras:
    palabras_transformadas.append(transformacion(palabra))
print(palabras_transformadas)

# Comprensión de listas con funciones

palabras_transformadas = [transformacion(palabra) for palabra in palabras]
# palabras_transformadas es una lista
print(palabras_transformadas) 

# Creación de un generador con comprensión de listas (ojo a los paréntesis en lugar de corchetes)
generador_palabras_transformadas = (transformacion(palabra) for palabra in palabras)
# generador_palabras_transformadas es un generador
print(generador_palabras_transformadas)
for palabra_transformada in generador_palabras_transformadas:
    print('Palabra transformada:', palabra_transformada)