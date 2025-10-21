class Pelicula:
    def __init__(self, titulo, director, recaudacion):
        self.titulo = titulo
        self.director = director
        self.recaudacion = recaudacion

    def guardar(self):
        # Guarda en un fichero que tendrá por nombre el título de la película y la extensión .movie
        with open(self.titulo.lower().replace(' ','_')+'.movie', mode='w', encoding='utf-8') as fichero:
            fichero.write(self.titulo)
            fichero.write('\n')
            fichero.write(self.director)
            fichero.write('\n')
            fichero.write(str(self.recaudacion))
            fichero.write('\n')

    @staticmethod
    def leer(titulo_a_leer) -> Pelicula:
        try:
            with open(titulo_a_leer.lower().replace(' ','_')+'.movie', mode='r', encoding='utf-8') as fichero:
                titulo = fichero.readline().replace('\n','')
                director = fichero.readline().replace('\n','')
                recaudacion = fichero.readline().replace('\n','')
            pelicula = Pelicula(titulo, director, recaudacion)
        except FileNotFoundError as fne:
            raise KeyError(f'La película {titulo_a_leer} no existe')
        return pelicula

    def __str__(self):
        return f'Título:{self.titulo}. Director:{self.director}. Recaudación:{self.recaudacion}'

    def __repr__(self):
        return self.__str__()

# Ejecución 1
# blade_runner = Pelicula('Blade Runner','Kubrick', 10_000)
# blade_runner.guardar()

# Ejecución 2
blade_runner = Pelicula.leer('Blade Runner')
print(blade_runner)

# Ejecución 3 - Controlando que el título (la clave) se corresponde con un fichero en el sistema de archivos
try:
    batman = Pelicula.leer('Batman')
except KeyError as ke:
    print(ke)