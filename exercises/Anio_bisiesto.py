# https://pywombat.com/my/exercises/ed6bd058

if __name__ == '__main__':
    year = int(input('Year: '))

    print('¡Año bisiesto!') if not year % 4 and year % 100 or not year % 400 else print('¡Año ordinario!')