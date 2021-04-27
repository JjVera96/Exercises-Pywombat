import string

def main():
    s = input('Cadena: ')
    result = ''
    for letter in s:
        if letter.lower() in string.ascii_lowercase:
            index = string.ascii_lowercase.index(letter.lower())
            result += '{} '.format(index+1)
    print(result)

if __name__ == '__main__':
    main()
