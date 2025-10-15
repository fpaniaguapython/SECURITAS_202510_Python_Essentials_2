import marketing
import rrhh
import tools
from util import gestor_email

if __name__ == '__main__':
    print('Este es el archivo principal')
    gestor_email.enviar_email('Todos los empleados', 'Reunión a las 10 AM')
    marketing.lanzar_campaña('Lanzamiento de nuevo producto')
    marketing.LANGUAGE = 'en'