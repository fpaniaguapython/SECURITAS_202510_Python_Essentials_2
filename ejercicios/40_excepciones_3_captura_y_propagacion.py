import enum

class Operacion(enum.Enum):
    SUMA = 1
    RESTA = 2
    MULTIPLICACION = 3
    DIVISION = 4

def dividir(dividendo, divisor):
    try:
        resultado = dividendo / divisor
    except ZeroDivisionError as zde:
        print('LOG: Ha ocurrido un error al tratar de dividir:', zde)
        raise zde
    return resultado

def calcular(operacion : Operacion, operando_1, operando_2):
    if (operacion==Operacion.DIVISION):
        try:
            resultado = dividir(operando_1, operando_2)
        except ZeroDivisionError as zde:
            print('LOG: No he podido calcular:', zde)
            raise zde
        return resultado
    
try:    
    resultado = calcular(Operacion.DIVISION, 10, 0)
    print(resultado)
except ZeroDivisionError as zde:
    print('LOG: Algo ha fallado')

