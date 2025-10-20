class Motor:
    def __init__(self, modelo):
        self.modelo = modelo
    def arrancar(self):
        print(f'Soy {self.modelo} y estoy arrancando')

motor = Motor('RR1004')
motor.arrancar()

motor.marca = 'Rolls-Royce' # Agregando un atributo a la instancia
print(motor.marca)

# Los métodos son 'atributos' de clase, por lo  tanto se tienen
# que asignar a la clase y NO al objeto
def stop(self):
    print(f'Soy {self.modelo} y estoy parando')

Motor.parar = stop #Agregando un método a la clase
motor.parar()

print(hasattr(motor, 'marca')) # True
print(hasattr(Motor, 'parar')) # True
print(hasattr(motor, 'parar')) # True, pero no es ejecutable 'directamente'