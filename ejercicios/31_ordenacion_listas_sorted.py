# ORDENACIÓN 'POR DEFECTO'

lista = [5, 8, 6, 2, 3, 4, 1] # Ordena 'bien'
lista = ['pan', 'Leche', 'sal', 'café'] # Ordena 'mal'
lista = [('pan', 2), ('azafrán',1), ('Batata', 8)] # Ordena 'mal'
lista = [(2, 'pan'), (1, 'azafrán'), (8, 'Batata')] # Ordena 'bien'
# lista = [('pan', 2), (1, 'azafrán'), ('Batata', 8)] # Error

# lista.sort() # Ordena la lista - Modifica la lista
nueva_lista = sorted(lista) # Genera una NUEVA LISTA ordenada
print(lista)
print(nueva_lista)

# ORDENACIÓN 'A MEDIDA'

items = [{'id':10_382, 'producto':'Clavos', 'cantidad':100, 'precio':20},
         {'id':10_385, 'producto':'Tornillos', 'cantidad':80, 'precio':40},
         {'id':10_403, 'producto':'Remaches', 'cantidad':50, 'precio':30},
         {'id':10_102, 'producto':'Tuercas', 'cantidad':200, 'precio':35}]

def ponderar(item : dict) -> int:
    return item.get('precio')

# Indicamos como key una función
print('***Usando sorted y función externa')
print(sorted(items, key=ponderar, reverse=True))
print(items) # Sigue teniendo el orden inical

# Indicamos como key una lambda
print('***Usando sorted y función lambda')
print(sorted(items, key=lambda item: item['cantidad']))

print('***Usando método sort y función externa')
items.sort(key=ponderar)
print(items)




