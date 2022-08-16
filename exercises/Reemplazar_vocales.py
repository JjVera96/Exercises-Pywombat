# https://pywombat.com/my/exercises/cdcee521

import re

if __name__ == '__main__':
    s = input('Cadena: ')
    result = re.sub(r'a|e|i|o|u', '@', s)
    print(result)