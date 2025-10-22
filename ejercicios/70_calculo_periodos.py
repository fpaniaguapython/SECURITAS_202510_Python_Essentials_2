import datetime

ahora = datetime.datetime.today()
print(f'Fecha actual:{ahora}') # Fecha actual:2025-10-22 10:12:09.362885
periodo = datetime.timedelta(days=4, hours=3)
fecha_finalizacion = ahora + periodo
print(f'Fecha finalización:{fecha_finalizacion}') # Fecha finalización:2025-10-26 13:12:09.362885