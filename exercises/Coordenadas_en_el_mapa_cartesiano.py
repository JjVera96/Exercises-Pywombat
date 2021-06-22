if __name__ == '__main__':
    x = int(input('x: '))
    y = int(input('y: '))

    if x == 0 and y == 0: print('Este es el origen!.')
    elif x == 0 or y == 0: print('Una de las coordenadas es igual a cero!.')
    elif x > 0:
        print('I') if y > 0 else print('IV')
    else: 
        print('II') if x > 0 else print('III')