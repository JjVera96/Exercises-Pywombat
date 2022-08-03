# https://pywombat.com/my/exercises/f331a39c

import re 

if __name__ == '__main__':
    string = 'Hola mundo desde Python en su versión 3.10'
    result = re.search('\d', string).group()
    
    if not result:
        print('Lo sentimos, el string no posee un número entero.')
    elif result == 1:
        print('El string solo posee un número entero.')
    else:
        print('El String posee {} números enteros.'.format(result))
