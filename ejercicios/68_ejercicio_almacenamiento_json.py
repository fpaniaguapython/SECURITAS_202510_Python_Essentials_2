import json

class Pelicula:
    def __init__(self, titulo, director, recaudacion, anyo):
        self.titulo = titulo
        self.director = director
        self.recaudacion = recaudacion
        self.anyo = anyo

    def guardar(self):
        # Guarda en un fichero que tendrá por nombre el título de la película y la extensión .movie
        with open(self.titulo.lower().replace(' ','_')+'.json', mode='w', encoding='utf-8') as fichero:
            json.dump(self.__dict__, fichero)

    @staticmethod
    def leer(titulo_a_leer) -> Pelicula:
        try:
            with open(titulo_a_leer.lower().replace(' ','_')+'.json', mode='r', encoding='utf-8') as fichero:
                atributos_pelicula = json.load(fichero) # Obtenemos un dict
                pelicula = Pelicula(**atributos_pelicula) # Desempaquetado del dicionario
        except FileNotFoundError as fne:
            raise KeyError(f'La película {titulo_a_leer} no existe')
        return pelicula

    def __str__(self):
        return f'Título:{self.titulo}. Director:{self.director}. Recaudación:{self.recaudacion}. Año:{self.anyo}'

    def __repr__(self):
        return self.__str__()

# Ejecución 1
# alien = Pelicula('Alien','Kevin', 20_000, 1985)
# alien.guardar()

# Ejecución 2
alien = Pelicula.leer('Alien')
print(alien)

# Ejecución 3 - Controlando que el título (la clave) se corresponde con un fichero en el sistema de archivos
# try:
#     batman = Pelicula.leer('Batman')
# except KeyError as ke:
#     print(ke)