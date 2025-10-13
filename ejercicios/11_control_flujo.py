lista = [1, 2, 3]

# Bucle for 'normal'
for elemento in lista:
    print(f'Elemento: {elemento}')

# Bucle for con función range()
for i in range(5): # Va de 0 a 4
    print(f'Índice: {i}')

# Bucle while
contador = 0
while contador < 3:
    print(f'Contador: {contador}')
    contador += 1

# if, elif, else
valor = 10
if valor < 5:
    print('Valor es menor que 5')
elif valor == 5:
    print('Valor es igual a 5')
else:
    print('Valor es mayor que 5')

# match-case (Python 3.10+) (similar a switch-case en otros lenguajes)
opcion = 'B'
match opcion:
    case 'A': # Equivalente al if
        print('Opción A seleccionada')
    case 'B': # Equivalente al elif
        print('Opción B seleccionada')
    case _: # Equivalente al else del if
        print('Opción no reconocida')