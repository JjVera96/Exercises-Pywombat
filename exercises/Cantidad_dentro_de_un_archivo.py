# https://pywombat.com/my/exercises/a01a1dae

if __name__ == '__main__':
    words = 0
    chars = 0
    name = input('Ingresa el nombre del archivo: ')
    with open(name) as file:
        for line in file.readlines():
            words += len(line.strip().split(' '))
            chars += len(line.strip())
    print(words, chars)
