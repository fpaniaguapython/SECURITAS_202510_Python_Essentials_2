'''
Queremos validar que se tiene el perfil adecuado para ejecutar una 
función. La validación se hace vía decorador.

El perfil se encuentra en una variable global llamada 'perfil'
que puede tener los valores USUARIO o ADMINISTRADOR
'''
from enum import Enum

class TipoPerfil(Enum):
    USUARIO = 0
    ADMINISTRADOR = 1

perfil = TipoPerfil.USUARIO

def validar_administrador(funcion_decorada):
    print('PASO 1') # Se ejecuta solo con decorar la función (no hace falta llamarla)
    def validar(*args, **kwargs):
        print('PASO 2') # Se ejecuta cuando se invoca la función
        if (perfil!=TipoPerfil.ADMINISTRADOR):
            raise Exception('El usuario no tiene el perfil administrador')
        return funcion_decorada(*args, **kwargs)
    print('PASO 3') # Se ejecuta solo con decorar la función (no hace falta llamarla)
    return validar
    

@validar_administrador
def saludar(nombre):
    return f'Hola {nombre}'

resultado = saludar('Python')
print(resultado)