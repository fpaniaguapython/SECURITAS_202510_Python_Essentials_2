import re

correo = 'fernando.paniagua@gmail.com' # OK
correo = 'malhecho#gmail.com' # KO
regexp = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

if re.fullmatch(regexp, correo):
    print('OK')
else:
    print('KO')