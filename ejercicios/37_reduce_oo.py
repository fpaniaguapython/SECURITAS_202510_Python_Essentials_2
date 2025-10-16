from functools import reduce

class Pelicula:
    def __init__(self, titulo, taquilla):
        self.titulo = titulo
        self.taquilla = taquilla

p1 = Pelicula('Alien', 1_000)
p2 = Pelicula('Tiburón', 2_000)
p3 = Pelicula('Nosferatur', 4_000)

peliculas = [p1, p2, p3]

# Reduce con función 'normal'
def acumular_taquilla(acumulado : int, pelicula : Pelicula):
    return acumulado + pelicula.taquilla

taquilla_acumulada = reduce(acumular_taquilla, peliculas, 0)
print(taquilla_acumulada) # 7000

# Reduce con función lambda
taquilla_acumulada = reduce(lambda acumulado, pelicula : acumulado + pelicula.taquilla, peliculas, 0)
print('#', taquilla_acumulada) # 7000