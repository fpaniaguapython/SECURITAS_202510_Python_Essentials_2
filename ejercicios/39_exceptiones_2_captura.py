dividendo = 100
lista = [0,1,2,3]
indice = 2

try:
    # Se ejecuta el bloque completo salvo que ocurra una excepción
    resultado = dividendo / lista[indice]
    print(resultado)
except ZeroDivisionError as zde:
    # Si ocurre un excepción, se ejecuta este bloque
    print('No se puede dividir entre 0:', zde)
except IndexError as ie:
    print('Estás intentado dividir entre algo que no existe', ie)
except BaseException as e:
    print('Ha ocurrido un error. Contacte con el administrador.', e)
else:
    print('Bloque else. Se ejecuta si NO HA OCURRIDO NINGUNA EXCEPCIÓN (ha ido todo bien)')
finally:
    print('Bloque finally. Se ejecuta SIEMPRE.')

# Este código se ejecuta después del tratamiento de la excepción (no depende)    
print('Fin del proceso')