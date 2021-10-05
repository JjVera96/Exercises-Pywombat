# https://pywombat.com/my/exercises/06176b0e

if __name__ == '__main__':
    my_list = []
    n = int(input('Longitud de la lista: '))

    for i in range(n):
        x = int(input('Ingresa un elemento: '))
        my_list.append(x)

    odd_max = max(list(filter(lambda x: x % 2 == 0, my_list)))

    print(odd_max)