class Pelicula:
    def __init__(self, titulo, director, recaudacion):
        self.titulo = titulo
        self.director = director
        self.recaudacion = recaudacion

    def guardar(self):
        # Guarda en un fichero que tendrá por nombre el título de la película y la extensión .movie
        pass

    @staticmethod
    def leer(titulo) -> Pelicula:
        pass


# Ejecución 1
blade_runner = Pelicula('Blade Runner','Kubrick', 10_000)
blade_runner.guardar()

# Ejecución 2
blade_runner = Pelicula.leer('Blade Runner')
print(blade_runner)

