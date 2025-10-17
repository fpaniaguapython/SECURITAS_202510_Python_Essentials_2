class Empleado:
    edad_minima = 18
    def __init__(self, nombre, id, salario):
        self.nombre = nombre
        self.id = id
        self.salario = salario

    def saludar(self):
        return f'Hola, soy {self.nombre}'

juanluis = Empleado('Juan Luis', 1838, 25_000)
print(juanluis.__dict__) # {'nombre': 'Juan Luis', 'id': 1838, 'salario': 25000}
print(Empleado.__dict__) # {'edad_minima': 18, '__init__': <function Empleado.__init__ at 0x000001F369ED3880>, 'saludar': <function Empleado.saludar at 0x000001F369ED39C0>}
rosa = Empleado('Rosa', 1841, 26_000)
print(rosa.__dict__) # {'nombre': 'Rosa', 'id': 1841, 'salario': 26000}
rosa.vacaciones_pendientes = 50 # Creando un atributo nuevo por asignación
setattr(rosa, 'pais', 'Argentina') # Creando un atributo nuevo mediante setattr
print(juanluis.__dict__)
print(rosa.__dict__)
del rosa.vacaciones_pendientes # Elimina el atributo vacaciones_pendientes del objeto rosa
print(rosa.__dict__)