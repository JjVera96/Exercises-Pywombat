# https://pywombat.com/my/exercises/e4d44b74

def longitud(s):
    lng = 0
    s = list(s)
    while s:
        s.pop()
        lng += 1
    return lng

if __name__ == '__main__':
    print(longitud('Hola'))
    print(longitud('Hola Mundo'))