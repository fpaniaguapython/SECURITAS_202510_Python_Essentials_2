# Lectura de fichero de texto
# Opción 1 - 'Tradicional'

print('******** OPCIÓN 1 - LECTURA TRADICIONAL ********')
fichero = open(file='63_ficheros_basico.py', mode='rt', encoding='utf-8')
contenido = fichero.read()
print(contenido)
fichero.close()

# Opción 2 - Utilizando with (hace el close de manera automática)

print('******** OPCIÓN 2 - LECTURA CON WITH ********')
with open(file='63_ficheros_basico.py', mode='rt', encoding='utf-8') as fichero:
    contenido = fichero.read()
    print(contenido)

# Opción 3 - Lectura de líneas

print('******** OPCIÓN 3 - LECTURA DE LÍNEAS ********')
with open(file='63_ficheros_basico.py', mode='rt', encoding='utf-8') as fichero:
    contenido = fichero.readlines() # Incluye en cada líneas los \n
    # contenido = [linea.replace('\n','') for linea in fichero.readlines()] # Eliminamos los \n
    print(contenido)

# Opción 4 - Lectura línea a línea

print('******** OPCIÓN 4 - LECTURA LÍNEA A LÍNEA ********')
with open(file='63_ficheros_basico.py', mode='rt', encoding='utf-8') as fichero:
    linea = fichero.readline()
    while (linea!=''):
        linea=linea.replace('\n','') # Eliminamos los \n de final de cada línea
        print(linea)        
        linea = fichero.readline()

# Opción 5 - Lectura como iterable

print('******** OPCIÓN 5 - LECTURA COMO ITERABLE ********')
with open(file='63_ficheros_basico.py', mode='rt', encoding='utf-8') as fichero:
    for linea in fichero:
        print(linea.replace('\n',''))

