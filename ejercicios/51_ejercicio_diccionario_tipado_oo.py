# Definir una clase Pelicula con los atributos Título y año.
# Construir una estructura de datos de tipo <dict> que sólo admita objetos Pelicula

class Movie:
    def __init__(self, title, year):
        self.title = title
        self.year = year

    def __str__(self):
        return f'Title:{self.title}. Year:{self.year}'
    
    def __repr__(self):
        return self.__str__()
    
class DictMovie(dict):
    @staticmethod
    def validate_value_type(obj : object):
        if (not isinstance(obj, Movie)):
            raise TypeError('Esta lista solo admite objetos <Movie>')

    def __init__(self, *args, **kwargs):
        print('Método __init__')
        for movie in kwargs.values():
            DictMovie.validate_value_type(movie)
        super().__init__(*args, **kwargs)

    def __setitem__(self, key, value):
        print('Método __setimtem__')
        DictMovie.validate_value_type(value)
        return super().__setitem__(key, value)
    
    def update(self, *args, **kwargs):
        print('Método update')
        for items in args: # args es una tupla de diccionarios (solo lleva uno)
            for movie in items.values(): # items es un dict
                DictMovie.validate_value_type(movie)
        super().update(*args, **kwargs)

movie_1 = Movie('E.T.', 1982)
movie_2 = Movie('Alien', 1986)

movies = DictMovie(uno=movie_1, dos=movie_2) # OK
# movies = DictMovie(uno=movie_1, dos=movie_2, tres='grillo') # Error

movies['tres']=Movie('Tiburón', 1988)
# movies['cuatro']='grillo' # Error

# movies.update({'cinco': Movie('Superman',1981)})
# movies.update({'seis': 'grillo'}) # Error

movies.update({'cinco': Movie('Superman',1981), 'seis': Movie('El hombre invisible', 2004)})
# movies.update({'cinco': Movie('Superman',1981), 'seis': Movie('El hombre invisible', 2004), 'siete': 'grillo'}) # Error

print(movies)
