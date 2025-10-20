# Esto es algo parecido a una interface
class IAlmacenDatos:
    def guardar(self, clave : str, datos : str):
        raise NotImplementedError('El método guardar no está implementado')

    def recuperar(self, clave : str) -> str:
        raise NotImplementedError('El método recuperar no está implementado')

# Esta clase implementa la interface
class AlmacenDatosEnFichero(IAlmacenDatos):
    NOMBRE_FICHERO = 'almacen.txt'
    def guardar(self, clave : str, datos : str):
        with open(AlmacenDatosEnFichero.NOMBRE_FICHERO, 'a', encoding='utf-8') as fichero:
            fichero.write(f'{clave}:{datos}\n')

    def recuperar(self, clave):
        return (f'Datos leidos de la clave {clave}')

# Esta clase implementa erroneamente la interface
class AlmacenDatosFake(IAlmacenDatos):
    pass

# Esto es una versión 'reducida y simplicada' del patrón de diseño Factory
def almacen_factory():
    return AlmacenDatosEnFichero()

def guardar_datos(clave, datos):
    almacen = almacen_factory()
    if (isinstance(almacen, IAlmacenDatos)):
        almacen.guardar(clave, datos)
    else:
        print('Error: el almacén no es un almacén')

guardar_datos('Segmento_1', 'Datos inventados')