# https://pywombat.com/my/exercises/3f867f4b

if __name__ == '__main__':
    row = int(input('Fila: '))
    col = int(input('Columna: '))

    if (row == 1 and (col == 1 or col == 8)) or (row == 8 and (col == 1 or col == 8)):
        print(3)
    elif ((row == 1 or row == 8) and (col > 1 or col < 8)) or ((col == 1 or col == 8) and (row > 1 or row < 8)):
        print(5)
    else:
        print(8)

