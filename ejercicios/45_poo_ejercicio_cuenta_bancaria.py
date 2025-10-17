'''
Crear una clase cuenta bancaria
Atributos: Nombre del cliente, número de cuenta, estado y el saldo.
Estado puede ser ACTIVA, SUSPENDIDA, DESCUBIERTA -- Enumeraciones
Métodos: 
- incrementar_importe, incrementa el saldo (sólo puede recibir enteros positivos) -- assert
----- Si la cuenta está SUSPENDIDA, lanza una excepción SUSPENDIDA_EXCEPTION (excepción propia)
----- Si el saldo después de ingresar un importe pasa a positivo, pasamos el estado ACTIVA
- retirar_importe, decrementa el saldo (sólo puede recibir enteros negativos) -- assert
----- Si la cuenta está SUSPENDIDA, lanza una excepción SUSPENDIDA_EXCEPTION (excepción propia)
----- Si el saldo después de retirar un importe pasa a negativo, pasamos el estado DESCUBIERTA

Crear una cuenta, hacer operaciones con ella y mostrar los atributos de la cuenta por pantalla (__str__ y __repr__)
'''
from enum import Enum

class Estado(Enum):
    ACTIVA = 1
    SUSPENDIDA = 2
    DESCUBIERTA = 3

class SuspendidaException(Exception):
    def __init__(self, *args):
        super().__init__(*args) # Invocación al constructor de la clase padre

class Cuenta:
    def __init__(self, cliente : str, numero : str, estado : Estado, saldo : int):
        self.cliente = cliente
        self.numero = numero
        self.estado = estado
        self.saldo = saldo

    def incrementar_importe(self, incremento : int):
        print(f'Intentando incrementar el saldo en {incremento}')
        assert(isinstance(incremento, int))
        assert(incremento>0)
        if (self.estado==Estado.SUSPENDIDA):
            raise SuspendidaException('La cuenta está suspendida')
        saldo_anterior = self.saldo
        self.saldo+=incremento
        if (saldo_anterior<0 and self.saldo>=0):
            self.estado=Estado.ACTIVA

    def retirar_importe(self, decremento : int):
        print(f'Intentando decrementar el saldo en {decremento}')
        assert(isinstance(decremento, int))
        assert(decremento<0)
        if (self.estado==Estado.SUSPENDIDA):
            raise SuspendidaException('La cuenta está suspendida')
        saldo_anterior = self.saldo
        self.saldo+=decremento
        if (saldo_anterior>=0 and self.saldo<0):
            self.estado=Estado.DESCUBIERTA

    def __str__(self):
        return f'Cliente:{self.cliente}. Cuenta:{self.numero}. Estado:{self.estado}. Saldo:{self.saldo}'

    def __repr__(self):
        return self.__str__()
  

cuenta = Cuenta('Fernando','1234567890', Estado.ACTIVA, 10_000)
print(cuenta)
cuenta.retirar_importe(-5000)
print(cuenta)
cuenta.retirar_importe(-7000)
print(cuenta)
cuenta.incrementar_importe(2100)
print(cuenta)
cuenta.estado = Estado.SUSPENDIDA
cuenta.incrementar_importe(900)