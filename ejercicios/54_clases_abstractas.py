from abc import ABC, abstractmethod # Módulo de clases abstractas https://docs.python.org/es/3.13/library/abc.html

class AlmacenAbstracto(ABC):
    def __init__(self, nombre_almacen):
        print('En el __init__')
        self.nombre_almacen = nombre_almacen

    @abstractmethod
    def guardar(self, clave : str, datos : str):
        pass

    @abstractmethod
    def recuperar(self, clave : str) -> str:
        pass

    def mostrar_nombre(self):
        print(f'Nombre:{self.nombre_almacen}')

class AlmacenFichero(AlmacenAbstracto):
    def __init__(self, nombre_almacen):
        super().__init__(nombre_almacen)

    def guardar(self, clave : str, datos : str):
        print('Guardando...')

    def recuperar(self, clave : str) -> str:
        print('Recuperando...')

almacen_fichero = AlmacenFichero('mialmacen')
almacen_fichero.mostrar_nombre()
 