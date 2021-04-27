def main():
    cash = int(input('Dinero: '))

    if cash < 15:
        print('No dispone de suficiente dinero!')
    elif cash < 80:
        print('Usted ha comprado {} gallinas !!'.format(cash//15))
    elif cash < 150:
        print('Usted ha comprado {} cabras !!'.format(cash//50))
    elif cash < 500:
        print('Usted ha comprado {} cerdos !!'.format(cash//150))
    elif cash < 1500:
        print('Usted ha comprado {} vacas !!'.format(cash//500))
    else:
        print('Usted ha comprado {} panales !!'.format(cash//1500))


if __name__ == '__main__':
    main()
