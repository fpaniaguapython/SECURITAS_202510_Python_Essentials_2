fichero = open("datos.txt", "r", encoding="utf-8")
lineas = fichero.readlines()
for linea in lineas:
    #print(linea[0:len(linea)-1])
    print(linea[:-1])
fichero.close()