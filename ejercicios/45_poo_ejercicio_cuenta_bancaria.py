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