# https://pywombat.com/my/exercises/84c56c18

if __name__ == '__main__':
    string = input('Ingresa un string: ')
    result = ''
    for c in string:
        if c in 'aeiou':
            c = c.upper()
        result += c
    print(result)
        
