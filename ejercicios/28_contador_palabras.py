'''
Obtener el número de palabras distintas que aparecen en el fichero
'elquijote.txt'
'''

## Paso 2. Leer el fichero

with open('elquijote.txt', mode='r', encoding='utf-8') as fichero:
  texto = fichero.read()

"""## Paso 3. Mostrar el contenido leído del fichero"""

print(texto)

"""## Paso 4. Limpiar de símbolos el texto
Sustituye cada uno los caracteres de la variable 'simbolos' por un espacio en blanco.
"""

simbolos = '.;,'
texto_limpio=texto
for simbolo in simbolos:
  texto_limpio = texto_limpio.replace(simbolo, ' ')

print(texto_limpio)

"""## Paso 5. Obtener los 'token'"""

lista_token = texto_limpio.split()

print(lista_token)

"""## Paso 6. Convertir los token a minúscula"""

lista_token_minuscula = [token.lower() for token in lista_token]

print(lista_token_minuscula)
print('Número de elementos de la lista:',len(lista_token_minuscula))

"""## Paso 7. Convertir a conjunto"""

conjunto_tokens = set(lista_token_minuscula)

"""## Paso 8. Contar el número de tokens del conjunto"""

print(conjunto_tokens)
print('Número de elementos distintos del texto:', len(conjunto_tokens))

