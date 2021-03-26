file_name = input('Ingresa el nombre del archivo: ')
chunk_size = int(input('Cantidad de palabras por bloque: '))

file = open(file_name)

while True:
    data = file.read(chunk_size)
    if not data:
        break
    print('{}\n\n\n'.format(data))
