
if __name__ == '__main__':
    vowels = 'aeiouAEIOU'

    s = input('Cadena: ')
    result = ''
    for c in s:
        if not c in vowels:
            result += c

    print(result)