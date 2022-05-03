# https://pywombat.com/my/exercises/04f4b36f

import math

if __name__ == '__main__':
    a = int(input('Aula1: '))
    b = int(input('Aula2: '))
    c = int(input('Aula3: '))

    print('Se deben comprar {} escritorios !!'.format(
        math.ceil(a/2) + math.ceil(b/2) + math.ceil(c/2)))