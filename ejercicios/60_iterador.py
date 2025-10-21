class Pelicula(object):
    def __init__(self, titulo, cast : list):
        self.titulo = titulo
        self.__cast = cast
        self.__current_position = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if (self.__current_position==len(self.__cast)):
            self.__current_position=0
            raise StopIteration()
        current_element = self.__cast[self.__current_position]
        self.__current_position+=1
        return current_element

pelicula_1 = Pelicula('Película 1', ['Actriz 1', 'Actor 1', 'Actor 2', 'Actriz 2', 'Actriz 3'])

for item in pelicula_1:
    print(item)

for item in pelicula_1:
    print(item)