if __name__ == '__main__':
    A = input('A: ')
    B = input('B: ')
    H = input('H: ')
    
    if int(A) > int(H): result = 'Deficiente'
    elif int(H) < int(B): result = 'Normal'
    else: result = 'Exceso'

    print(result)