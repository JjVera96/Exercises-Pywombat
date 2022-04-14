# https://pywombat.com/my/exercises/a31d0a85

if __name__ == '__main__':
    a = int(input('A: '))
    b = int(input('B: '))
    c = int(input('C: '))

    print('¡Es un triángulo!') if (a+b+c) == 180 else print('¡No es un triángulo!')