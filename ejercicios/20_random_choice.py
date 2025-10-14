import random

def get_nombres():
    nombres = ['Alejandro', 'Arancha', 'Begoña', 'José', 'Kevin', 'Marco', 'Marian']
    return nombres

def get_apellidos():
    apellidos = ['Martín', 'Rodríguez', 'López', 'Blanco', 'Redondo']
    return apellidos

def get_datos_empleados(nombres : list, apellidos : list, numero_empleados : int, info_salarial : tuple) -> list:
    empleados = list()
    for numero in range(numero_empleados):
        nombre = random.choice(nombres)
        apellido_1 = random.choice(apellidos)
        apellido_2 = random.choice(apellidos)
        salario = random.randrange(info_salarial[0], info_salarial[1], info_salarial[2])
        empleados.append((nombre, apellido_1, apellido_2, salario))
    return empleados

if __name__=='__main__':
    nombres = get_nombres()
    apellidos = get_apellidos()
    info_salarial = (20_000, 150_000, 1_000)
    empleados = get_datos_empleados(nombres, apellidos, 100, info_salarial)
    print(empleados)

    