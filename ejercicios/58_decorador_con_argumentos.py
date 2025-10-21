'''
Queremos validar que se tiene el perfil adecuado para ejecutar una 
función. La validación se hace vía decorador CON ARGUMENTOS.

El perfil se encuentra en una variable global llamada 'perfil'
que puede tener los valores USUARIO o ADMINISTRADOR
'''
from enum import Enum

class TipoPerfil(Enum):
    USUARIO = 0
    ADMINISTRADOR = 1

perfil = TipoPerfil.USUARIO

def validar_perfil(perfil_necesario):
    def outer_wrapper(funcion_decorada):
        def inner_wrapper(*args, **kwargs):
            if (perfil!=perfil_necesario):
                raise Exception('El usuario no tiene el perfil adecuado')
            return funcion_decorada(*args, **kwargs)
        return inner_wrapper
    return outer_wrapper

@validar_perfil(perfil_necesario=TipoPerfil.ADMINISTRADOR)
def saludar(nombre):
    return f'Hola {nombre}'

resultado = saludar('Python')
print(resultado)