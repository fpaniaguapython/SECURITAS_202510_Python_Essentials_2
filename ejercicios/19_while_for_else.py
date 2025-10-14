contador=0
while contador<10:
    contador+=1
    print(contador)
    if contador==5:
        break
else:
    print('else del while') # Solo se ejecuta si la condición del bucle deja de cumplirse

lista = [1,2,3,4,5,6,7,8,9,10]
for numero in lista:
    print(numero*2)
    if numero==4:
        break
else:
    print('else del for') # Solo se ejecuta si se recorre el iterable al completo