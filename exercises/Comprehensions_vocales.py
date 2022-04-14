# https://pywombat.com/my/exercises/9303efec

if __name__ == '__main__':
    msg = input('Ingresa el mensaje a convertir: Este mensaje debe finalizar sin vocales: ')
    result = ''.join([x for x in msg if not x in  'aeiouAEIOU'])
    print(result)