import json

# Lectura de JSON
with open('alien.json') as fichero:
    pelicula = json.load(fichero)
print(type(pelicula)) # dict
print(pelicula)
print(pelicula['titulo']) # acceso
print(pelicula.get('director')) # acceso

# Escritura de JSON
pelicula['director']='Ridley Scott'
with open('alien_ok.json',mode='w') as fichero:
    json.dump(pelicula, fichero)

# Almacenamiento en JSON de una clase

class  Pelicula:
    def __init__(self, titulo, genero):
        self.titulo = titulo
        self.genero = genero

    # Método nuevo y propio que genera un diccionario para la serialización de la pelicula
    def to_dict(self):
        return self.__dict__

star_wars = Pelicula('Star Wars Episodio IV ', 'Aventuras')
with open('star_wars.json', mode='w') as fichero:
    # json.dump(star_wars, fichero) # Error
    json.dump(star_wars.__dict__, fichero)

# Almacenamiento en JSON de una lista
indiana = Pelicula('Indiana Jones en busca del arca perdida', 'Aventuras')
peliculas = [star_wars, indiana]

with open('pelis_json.json', mode='w') as fichero:
    json.dump([pelicula.to_dict() for pelicula in peliculas], fichero)