nombre = "Diana"
edad = 30
ciudad = "Barcelona"

# Queremos mostrar 'Ana tiene 30 años y vive en Barcelona'

print(nombre, "tiene", edad, "años y vive en", ciudad)
frase = nombre + " tiene " + str(edad) + " años y vive en " + ciudad
print(frase)
# Usando f-string (formatted string)
print(f"{nombre} tiene {edad} años y vive en {ciudad}")