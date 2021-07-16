if __name__ == '__main__':
    days = int(input('Total de días: '))
    food = int(input('Costo de comida por día: '))
    transport = int(input('Costo del transporte: '))
    hotel = int(input('Costo por noche en el hotel: '))

    print('Costo total del viaje: ${}'.format((days*food)+(transport*2)+((days-1)*hotel)))