# https://pywombat.com/my/exercises/fa406879

from datetime import datetime
from dateutil.relativedelta import relativedelta


if __name__ == '__main__':
    date = input('Fecha DD/MM/YYYY: ')
    date = datetime.strptime(date, '%d/%m/%Y')
    today = datetime.now()
    years = relativedelta(today, date).years
    print('La edad es {} años !!'.format(years))
