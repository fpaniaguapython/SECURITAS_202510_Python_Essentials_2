import calendar

with open('calendario_2025.txt', 'w') as fichero:
    #fichero.write(calendar.calendar(2025))
    fichero.write(calendar.month(2025,10))