import logging
import datetime

def registrar_log(funcion_a_decorar):
    def inner_function(*args, **kwargs):
        logging.critical(f'{funcion_a_decorar.__name__}. {datetime.datetime.now()}')
        return funcion_a_decorar(*args, **kwargs)
    return inner_function

@registrar_log
def sumar(a, b):
    return a+b

@registrar_log
def saludar():
    print('Hola')

resultado = sumar(13,36)
print(resultado)

saludar()