# Generar un número aleatorio entero entre 1 y 10
# Pedir al usuario un número.
# Contar el número de veces que se equivoca
# Si acierta en menos de 4 intentos, es un adivino y si no es un fraude

import random

NUMERO_MINIMO = 1
NUMERO_MAXIMO = 4
NUMERO_INTENTOS_MAXIMO = 2

intentos = 0
numero_aleatorio = random.randint(NUMERO_MINIMO,NUMERO_MAXIMO)
while True:
    numero_usuario = int(input(f'Adivina el número [{NUMERO_MINIMO}-{NUMERO_MAXIMO}]:'))
    intentos+=1
    if numero_usuario==numero_aleatorio:
        break
    else:
        print('Error')
if (intentos>NUMERO_INTENTOS_MAXIMO):
    print('Eres un fraude')
else:
    print('Eres un adivino')
        
    