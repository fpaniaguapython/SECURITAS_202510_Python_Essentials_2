def sumar(sumando_1 : int, sumando_2 : int) -> int:
    '''
    Suma dos números enteros positivos y devuelve el resultado

    sumando_1: número entero positivo
    sumando_2: número entero negativo

    Devuelve el resultado de la suma
    '''
    assert(isinstance(sumando_1, int) and isinstance(sumando_2, int))
    assert(sumando_1>=0 and sumando_2>=0)

    return sumando_1+sumando_2

if __name__=='__main__':
    resultado = sumar(8,5)
    print(resultado)