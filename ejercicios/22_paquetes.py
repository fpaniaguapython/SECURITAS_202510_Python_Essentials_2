# Crear un paquete que va a contener un conjunto de utilidades
# Módulo calculadora: una calculadora.
# Módulo backup: métodos para hacer y recuperar un bakcup.
# Cada paquete tendrá su fichero de configuración con una o dos constantes
# Crear un script principal que utilice los módulos.

# El paquete se encuentra en la carpeta utilidades_22

import utilidades_22 # Importar (ejecutar) el __init__.py
from utilidades_22 import backup # Opción 1 de importación
import utilidades_22.calculadora # Opción 2 de importación

if __name__=='__main__':
    print(utilidades_22.VERSION)
    print(utilidades_22.get_version())
    backup.hacer_backup()
    utilidades_22.calculadora.calcular()