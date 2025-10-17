dividendo = 100
divisor = 0

try:
    # Se ejecuta el bloque completo salvo que ocurra una excepción
    resultado = dividendo / divisor
    print(resultado)
except ArithmeticError as zde:
    # Si ocurre un excepción, se ejecuta este bloque
    print('No se puede dividir entre 0:', zde)

# Este código se ejecuta después del tratamiento de la excepción (no depende)    
print('Fin del proceso')