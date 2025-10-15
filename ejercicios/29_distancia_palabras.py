# pip install python-Levenshtein

import Levenshtein

ingredientes = ('arroz','azúcar','leche','sal','aceite','remolacha')

ingrediente_buscado = input('Introduce un ingrediente:')

ingredientes_con_distancia = list()
for ingrediente_candidato in ingredientes:
    distancia = Levenshtein.distance(ingrediente_buscado, ingrediente_candidato)
    ingredientes_con_distancia.append((distancia, ingrediente_candidato))

ingredientes_con_distancia.sort()

ingrediente_mas_proximo = ingredientes_con_distancia[0]

if (ingrediente_mas_proximo[0]==0):
    print(f'Aquí tienes tu {ingrediente_mas_proximo[1]}')
else:
    print(f'¿Quieres decir {ingrediente_mas_proximo[1]}?')