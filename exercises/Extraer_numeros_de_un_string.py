if __name__ == '__main__':
    result = []
    num = ''
    s = input('Ingrese un string: ')

    for i, c in enumerate(s):
        if c.isdigit():
            num += c
        elif c == '.' and i != len(s)-1:
            if num != '':
                if s[i+1].isdigit():
                    num += c
        else:
            if num != '':
                result.append(num)
                num = ''

    print(result)
