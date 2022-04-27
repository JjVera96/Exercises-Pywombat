# https://pywombat.com/my/exercises/fa9d69bc

def cubo(i):
    return 4**3 < i**3 and i**3 < 9**3

if __name__ == '__main__':
    print(cubo(12))
    print(cubo(5))
    print(cubo(9))
