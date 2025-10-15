'''
Leer el fichero datos_27.txt
y mostrar por pantalla el número de incidencia
1. Leer el fichero
2. Recorrer línea a línea
3. Eliminar el salto de línea (opcional)
4. Obtener el código de incidencia.
5. Procesar el código.
'''
def get_file_lines(file_name):
    with open(file_name, mode='r', encoding='utf-8') as data_file:
        lines = data_file.readlines()
    return lines

def clear_lines_break(lines):
    for index, line in enumerate(lines):#Forma de iterar por una lista (o similar) obteniendo índice y valor
        if ('\n' in line):
            line = line[:line.index('\n')]
            # line = line[:-1] # Hace lo mismo que la línea anterior
            lines[index]=line
    return lines

def get_error_codes(lines):
    code_list = []
    for line in lines:
        code_list.append(line[:line.index('#')])
    return code_list

if __name__=='__main__':
    lines = get_file_lines('datos_27.txt')
    clear_lines = clear_lines_break(lines)
    code_list = get_error_codes(clear_lines)
    print(code_list)