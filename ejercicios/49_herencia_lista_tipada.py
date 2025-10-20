lista = [1,2,3]
lista = list()

lista.append(1)
lista.insert(0,2)

print(lista)

lista[0]=1
lista[1]=2

print(lista)

class ListaEnteros(list):
    def __init__(self, *args):
        print('Método __init__')
        for arg in args:
            if (not isinstance(arg, int)):
                raise TypeError('Esta lista solo admite objetos <int>')
        super().__init__(args)

    def append(self, value):
        print('Método append')
        if (not isinstance(value, int)):
            raise TypeError('Esta lista solo admite objetos <int>')
        return super().append(value)
    
    def insert(self, index, value):
        if (not isinstance(value, int)):
            raise TypeError('Esta lista solo admite objetos <int>')
        return super().insert(index, object)

    def __setitem__(self, index, value):
        print('Método __setitem__')
        if (not isinstance(value, int)):
            raise TypeError('Esta lista solo admite objetos <int>')
        return super().__setitem__(index, value)

lista_enteros = ListaEnteros(1,2,3)
lista_enteros.append(8)
lista_enteros[3]=4

print(lista_enteros) # [1, 2, 3, 4]
print(lista_enteros[2]) # 3 --> Muestra la posición 2
del lista_enteros[1] # Elimina la posición 1
print(lista_enteros) # [1, 3, 4]
lista_enteros.pop() # Devuelve y elimina el último elemento
print(lista_enteros) # [1, 3]

lista_enteros.insert(0,10)
# lista_enteros.insert(0,'Diez') # Error