# https://pywombat.com/my/exercises/76044c9a

def palindromo(string):
    return string.lower().replace(' ', '') == string.lower().replace(' ', '')[::-1]

if __name__ == '__main__':
    strings = [
        'Estamos en un ejercicio en PyWombat',
        'Anita lava la tina', 'Amar da drama',
        'Este no es un string palindromo',
        'Ana lava lana'
        ]

    total = sum([palindromo(string) for string in strings])
    print('Cantidad de palindromos: {}'.format(total))