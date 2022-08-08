# https://pywombat.com/my/exercises/06c28b7e

import re

def main():
    ls = ['Pywombat exercises',
    'pywombat exercises',
    'Exercises Pywombat',
    'Exercises exercises']
    
    regex = re.compile(r'^pywombat\s')

    for s in ls:
        print(True if regex.search(s.lower()) else False) 
        
if __name__ == '__main__':
    main()