import csv

print('********************************')

# Lectura 'normal' (mediante reader). Devuelve una relación de listas con los elementos
with open('contacts.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        print('Row:',row) # Una lista con dos elementos
        print('Nombre:',row[0], 'Teléfono:', row[1])


print('********************************')

# Lectura 'especial' (mediante dictreader). Devuelve una relación de listas con los elementos
with open('contacts.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=',')
    for row in reader:
        print('Row:',row) # Un diccionaro que tiene como clave los valores del encabezado
        print('Nombre:',row['Name'], 'Teléfono:', row['Phone'])   

print('********************************')

# Lectura 'especial' (mediante dictreader). 
# En este caso el CSV no tiene encabezados

with open('contacts_sin_encabezado.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile, fieldnames=['Apodo','Contacto'], delimiter=',')
    for row in reader:
        print('Row:',row) # Un diccionaro que tiene como clave los valores del encabezado
        print('Nombre:',row['Apodo'], 'Teléfono:', row['Contacto'])  