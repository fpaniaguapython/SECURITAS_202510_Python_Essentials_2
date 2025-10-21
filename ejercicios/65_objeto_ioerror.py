import errno

try:
    with open('fichero_inexistente.txt', mode='r') as fichero:
        fichero.read()
except OSError as oe:
    print(oe.errno)
    print(oe.filename)
    if (oe.errno==errno.ENOENT):
        print(f'Fichero {oe.filename} no encontrado')
