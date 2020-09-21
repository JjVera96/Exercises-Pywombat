import datetime 

months_in_spanish = {
    1: 'Enero',
    2: 'Febrero',
    3: 'Marzo',
    4: 'Abril',
    5: 'Mayo',
    6: 'Junio',
    7: 'Julio',
    8: 'Agosto',
    9: 'Septiembre',
    10: 'Octubre',
    11: 'Noviembre',
    12: 'Diciembre',
    
}

def formato_fecha(date):
    return '{} de {} del {}'.format(date.day, months_in_spanish[date.month], date.year)

fecha = datetime.datetime(2020, 5, 7)
print(formato_fecha(fecha))

fecha = datetime.datetime(2029, 8, 17)
print(formato_fecha(fecha))

fecha = datetime.datetime.now()
print(formato_fecha(fecha))