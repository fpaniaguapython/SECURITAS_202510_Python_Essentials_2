# Paso de argumentos por valor
def calcular(argumento):
    argumento+=20 # Es lo mismo que argumento = argumento + 20
    print(f'Dentro de la función, el valor de argumento es: {argumento}')

entrada = 10
calcular(entrada)
print('En el ámbito global, el valor de entrada es:', entrada)

# Paso de argumentos por referencia ¡CUIDADO!
def calcular_lista(argumento):
    argumento.append(4)
    print(f'Dentro de la función, la lista (argumento) es:" {argumento}')

lista_entrada = [1, 2, 3]
calcular_lista(lista_entrada)
print('En el ámbito global, la lista (lista_entrada) es:', lista_entrada)



