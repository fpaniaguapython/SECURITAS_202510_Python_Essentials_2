import enum

class Estado(enum.Enum):
    VIVO = 0
    MUERTO = 1
    INMUNE = 2

#Definición de la clase
class Punto3D:
    # Constructor
    def __init__(self, x : int, y : int, z : int):
        self.x = x # self.x = x es la declaración e inicialización del atributo
        self.y = y
        self.z = z

    def __str__(self):
        return f'x:{self.x} y:{self.y} z:{self.z}'
    
    def __repr__(self):
        return self.__str__()

# Instanciación de un objeto de la clase Punto3D
punto_3d_ejemplo=Punto3D(50,0,0) 

# Acceso a los compontentes del objeto
print("Z antes de incrementar:", punto_3d_ejemplo.z)
punto_3d_ejemplo.z+=1
print("Z antes después de incrementar:", punto_3d_ejemplo.z)

class Enemigo:
    salud_inicial = 100 # Atributo de clase
    # Atributos --> Definen el estado
    def __init__(self, nombre : str, posicion : Punto3D, estado : Estado):
        self.nombre = nombre
        self.posicion = posicion
        self.estado = estado
        self.salud = Enemigo.salud_inicial # Enemigo.salud es el atributo de clase

    # Métodos --> Definen el comportamiento
    def avanzar(self, delta):
        self.posicion.z+=delta

    def recibir_danyo(self, merma):
        self.salud-=merma

    def __str__(self):
        return(f'Nombre:{self.nombre}. Salud:{self.salud}. Posicion:{self.posicion}')

    def __repr__(self):
        return self.__str__()

sauron = Enemigo('Sauron', Punto3D(10,0,50), Estado.VIVO)
sauron.avanzar(delta=2)
sauron.avanzar(delta=4)
sauron.recibir_danyo(50)
print([sauron])
