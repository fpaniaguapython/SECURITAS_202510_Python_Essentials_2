def sumar(sumando_1 : int, sumando_2 : int) -> int:
    '''
    Suma dos números enteros positivos y devuelve el resultado

    sumando_1: número entero positivo
    sumando_2: número entero negativo

    Devuelve el resultado de la suma
    '''
    if not isinstance(sumando_1, int) or not isinstance(sumando_2, int):
        raise TypeError('Los sumandos deben de tipo entero')
    if sumando_1<0 or sumando_2<0:
        raise ValueError('Los sumandos tienen que ser números positivos')

    return sumando_1+sumando_2

if __name__=='__main__':
    resultado = sumar(-3,4)
    print(resultado)