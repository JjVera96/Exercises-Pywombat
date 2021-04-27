def main():
    decimal = int(input('Número decimal: '))
    binary = str(bin(decimal))[2:]
    print('Número binario: {}'.format(binary))

if __name__ == '__main__':
    main()
