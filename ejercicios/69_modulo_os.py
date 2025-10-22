import os

if __name__=='__main__':
    retorno = os.system('python 69_modulo_os_funcion_externa.py')
    # retorno = os.system('"C:\Program Files\Google\Chrome\Application\chrome.exe" https://www.as.com')
    print('RETORNO:', retorno)
    if (retorno==0):
        print('El proceso se ha ejecutado satisfactoriamente')
    else:
        print('Ha habido un error durante la ejecución del proceso')