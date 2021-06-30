if __name__ == '__main__':
    kg = 2.205
    min_weight = int(input('Peso mínimo en lb: '))
    max_weight = int(input('Peso máximo en lb: '))
    weight = int(input('Peso diario en Kg: '))

    if weight*kg < min_weight:
        print('Tiene {} lb de bajo peso'.format(round(min_weight-(weight*kg)),2))
    elif weight*kg <= max_weight:
        print('Peso normal')
    else: 
        print('Tiene {} lb de sobrepeso'.format(round(max_weight-(weight*kg)),2))
