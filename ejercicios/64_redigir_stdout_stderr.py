import sys

# Redirigimos la salida estándar a un fichero
sys.stdout = open('salida_estandar.txt','at',encoding='utf-8')
print('Este texto se deberá escribir en el fichero salida_estandar.txt')
sys.stdout.close()

# Redirigimos la salida de error a un fichero
sys.stderr = open('salida_err.txt','at',encoding='utf-8')
resultado = 8/0 # El error se redirige al fichero 'salida_err.txt'
sys.stderr.close()