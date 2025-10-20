class Empleado:
    edad_minima = 18
    def __init__(self, nombre, id, salario):
        self.nombre = nombre
        self.id = id
        self.__salario = salario # Atributo 'privado'

    def saludar(self):
        return f'Hola, soy {self.nombre} y cobro {self.__salario}'
    
    def get_salario(self):
        return self.__salario
    
    def __subir_salario(self, incremento):
        self.__salario+=incremento
    

arancha = Empleado('Arancha', 1034, 30_000)
arancha.nombre = 'Aranzazu'
#print(arancha.__salario) # Error
print(arancha._Empleado__salario) # 30000
print(arancha.__dict__)
print(arancha.saludar())
# arancha.__subir_salario(1000) # Error
arancha._Empleado__subir_salario(1000)

print('*', arancha.__dict__)
arancha.__salario = 5000 # ¡OJO! Esta sentencia crea un nuevo atributo __salario
print(arancha.__dict__)
