dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
trastero = ["Cuchara", 23, True, 4.56]
todo = [dias, trastero, "Otra cosa"]
otra_lista = list() # Función built-in para crear listas
otra_lista.append("Elemento 1")
otra_lista.append("Elemento 2")

dias.append("Finde") # Agrega un elemento al final de la lista

print(dias)
print(trastero)
print(todo)
print(otra_lista)

for dia in dias:
    print("-", dia)
    print('x')

print("Tamaño de la lista 'dias':", len(dias)) # Función built-in para obtener el tamaño de la lista

lista_vacia = []
