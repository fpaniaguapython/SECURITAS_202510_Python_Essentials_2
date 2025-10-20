def ejecutar(funcion):
    print(funcion())

def externa(nombre):
    nombre_mayusculas = nombre.upper()
    def interna():
        return nombre_mayusculas
    return interna

if __name__=='__main__':
    funcion_obtenida = externa("Estefanía")
    ejecutar(funcion_obtenida)