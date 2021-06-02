from datetime import datetime

def get_date_by_month(year, month):
    try:
        date = datetime.strptime('{} {}'.format(year, month), '%Y %B')
    except ValueError:
        date = datetime.now()
    return date


if __name__ == '__main__':
    print(get_date_by_month(2021, 'February'))
    print(get_date_by_month(2018, 'December'))
    print(get_date_by_month(2000, 'August'))
    print(get_date_by_month(2000, 'EXAMPLE'))

