# Definir una clase Pelicula con los atributos Título y año.
# Construir una estructura de datos de tipo <list> que sólo admita objetos Pelicula

class Movie:
    def __init__(self, title, year):
        self.title = title
        self.year = year

    def __str__(self):
        return f'Title:{self.title}. Year:{self.year}'
    
    def __repr__(self):
        return self.__str__()

class ListMovie(list):
    @staticmethod
    def validate_type(obj : object):
        if (not isinstance(obj, Movie)):
            raise TypeError('Esta lista solo admite objetos <Movie>')
        
    # Alternativa al staticmethod
    # @classmethod
    # def validate_type(cls, obj : object):
    #    if (not isinstance(obj, Movie)):
    #       raise TypeError('Esta lista solo admite objetos <Movie>')

    def __init__(self, *args):
        print('Método __init__')
        for arg in args:
            ListMovie.validate_type(arg)
        super().__init__(args)

    def append(self, value):
        print('Método append')
        ListMovie.validate_type(value)
        return super().append(value)
    
    def insert(self, index, value):
        print('Método insert')
        ListMovie.validate_type(value)
        return super().insert(index, value)

    def __setitem__(self, index, value):
        print('Método __setitem__')
        ListMovie.validate_type(value)
        return super().__setitem__(index, value)

movie_1 = Movie('E.T.', 1982)
movie_2 = Movie('Alien', 1986)

movie_list = ListMovie(movie_1, movie_2)
# movie_list = ListMovie(movie_1, movie_2, 'Spiderman') # Error
print(movie_list)

movie_list.append(Movie('Batman',1987))
# movie_list.append('Spiderman') # Error

movie_list.insert(0, Movie('Julk', 1990))
# movie_list.insert(0, 'Julk') # Error

movie_list[0]=Movie(title='Hulk', year=1990)
# movie_list[0] = 'Hulk' # Error

print(movie_list)

elpadrino = Movie('El padrino', 1998)