if __name__ == '__main__':
    w = int(input('Peso: '))
    s = float(input('Altura: '))

    imc = w/(s**2)

    if imc < 18.5:
        print('Bajo peso')
    elif imc < 24.9:
        print('Normal')
    elif imc < 29.9:
        print('Sobrepeso')
    else:
        print('Obeso')
