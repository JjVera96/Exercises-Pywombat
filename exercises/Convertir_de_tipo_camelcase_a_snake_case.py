def camelcase_to_snake_case(s):
    out = ''
    for i in range(len(s)):
        if not s[i].islower():
            out += '{}'.format(s[i].lower() if i == 0 else '_' + s[i].lower())
        else:
            out += s[i]
    return out

def main():
    print(camelcase_to_snake_case('EjemploCamelCase'))
    print(camelcase_to_snake_case('EstoyAprendiendoPython'))

if __name__ == '__main__':
    main()
