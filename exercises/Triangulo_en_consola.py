# https://pywombat.com/my/exercises/6f2f3ff3

if __name__ == '__main__':
    n = int(input('Ingresa la cantidad de filas: '))

    for i in range(1, n + 1):
        print(' ' *(n - i) + '*' * (i + (i - 1)))