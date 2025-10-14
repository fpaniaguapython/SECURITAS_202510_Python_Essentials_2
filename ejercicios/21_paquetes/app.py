import common.log_system as log_system
import util.calculator

if __name__=='__main__':
    print(log_system.nombre_fichero)
    print(log_system._limite) # _limite es visible, pero no debería usarse (oculto)
    print(log_system.__rango) # __limite es visible, pero no debería usarse (oculto)