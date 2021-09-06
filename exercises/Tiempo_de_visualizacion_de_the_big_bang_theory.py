if __name__ == '__main__':
    serie_mins = 23 * 279
    daily = int(input('Minutos disponibles diarios: '))
    weekend = int(input('Minutos disponibles el fin de semana: '))

    print('{} días'.format(serie_mins/((daily*5)+weekend)))
    