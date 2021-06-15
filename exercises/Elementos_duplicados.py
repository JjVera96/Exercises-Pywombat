if __name__ == '__main__':
    n = int(input('Longitud de la lista: '))
    nums = []
    rep = []
    for _ in range(n):
        x = input('Ingresa un elemento: ')
        rep.append(x) if x in nums else nums.append(x)

    print(rep) if len(rep) else print('No existen elementos duplicados.')
    