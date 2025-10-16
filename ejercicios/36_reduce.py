from functools import reduce

numeros = [3, 4, 5, 10]

# reduce con lambda
resultado = reduce(lambda x,y: x+y, numeros, 0)
print(resultado) #22

# reduce con función 'convencional'
def reducir(x,y):
    return x+y

resultado = reduce(reducir, numeros, 10)
print(resultado) #32, porque pusimos 10 como valor inicial




