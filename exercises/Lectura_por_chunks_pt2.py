if __name__ == '__main__':
    name = input('Ingresa el nombre del archivo: ')
    num = int(input('Cantidad de palabras por bloque: '))

    try:
        file = open(name, 'r')
    except IOError:
        file = None
    
    print(file)
    
    if file:
        words = file.read().split(' ')
        aux = 0
        while aux < len(words):
            print('{}\n\n\n'.format(' '.join(words[aux: aux+num])))
            aux += num
