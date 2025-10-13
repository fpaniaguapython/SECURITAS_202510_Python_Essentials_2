frutas_invierno = ['naranja', 'mandarina', 'naranja', 'kiwi']
frutas_verano = ['sandía', 'melón', 'cereza', 'naranja']

# Utilizando conjuntos (set) obtener la lista de frutas comunes.
conjunto_frutas_invierno = set(frutas_invierno)
conjunto_frutas_verano = set(frutas_verano)
frutas_comunes = conjunto_frutas_invierno.intersection(conjunto_frutas_verano)
print("Frutas comunes:", frutas_comunes)

# Obtener la lista de frutas de verano que no son en invierno.
frutas_solo_verano = conjunto_frutas_verano.difference(conjunto_frutas_invierno)
print("Frutas solo de verano:", frutas_solo_verano)


