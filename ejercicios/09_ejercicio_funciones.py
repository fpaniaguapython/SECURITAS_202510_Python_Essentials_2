# Un comentario de una línea

'''
Crear un función que reciba dos listas
con marcas de automóviles y devuelva
una lista con las marcas comunes
'''
lista_1 = ['Ford', 'Toyota', 'Chevrolet', 'Honda']
lista_2 = ['BMW', 'Audi', 'Toyota', 'Honda']

def get_marcas_comunes(lista_1 : list, lista_2 : list) -> list:
    conjunto_1 = set(lista_1)
    comunes = conjunto_1.intersection(lista_2)
    return list(comunes)

marcas_comunes = get_marcas_comunes(lista_1, lista_2)
print("Marcas comunes:", marcas_comunes)