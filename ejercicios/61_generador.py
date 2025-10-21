import time

# Solución 'convencional'
def convertir_a_title(nombres : list):
    nombres_title = [nombre.title() for nombre in nombres]
    return nombres_title

nombres = ['arancha', 'begoña', 'jose david', 'jose omar', 'KEVIN', 'mARco']
nombres_convertidos = convertir_a_title(nombres)

print(nombres)
print(nombres_convertidos)

# Solución con generador

def convertir_a_title(nombres : list):
    for nombre in nombres:
        time.sleep(1) # Tarda 3 segundos en hacer el proceso
        yield nombre.title()

nombres = ['arancha', 'begoña', 'jose david', 'jose omar', 'KEVIN', 'mARco']

for nombre_convertido in convertir_a_title(nombres):
    print('Nombre convertido:', nombre_convertido)