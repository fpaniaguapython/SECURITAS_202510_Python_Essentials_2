class EmailValueError(ValueError):
    def __init__(self, *args, nombre_usuario):
        super().__init__(*args)
        self.nombre_usuario = nombre_usuario

    def enviar_email(self):
        print(f'Enviando email a {self.nombre_usuario}')

def notificar(nombre_usuario : str, email : str, mensaje : str):
    if '@' not in email:
        raise EmailValueError('Error de email', nombre_usuario='Fernando')
    print('El email se ha enviado')

try:
    notificar('Fernando', 'fernando.paniagua#gmail.com', '¿Cómo estás?')
except EmailValueError as eve:
    print("*", eve)
    eve.enviar_email()
    