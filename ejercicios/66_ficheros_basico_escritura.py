lista = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes']

with open(file='mi_salida.log', mode='wt', encoding='utf-8') as fichero:
    # Línea a línea
    # for elemento in lista:
    #    fichero.write(elemento)

    # El iterable al completo
    fichero.writelines(lista)