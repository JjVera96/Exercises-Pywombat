# https://pywombat.com/my/exercises/9f75110b

def cuadra(n):
    print('*'*n)
    print(('*' + ' '*(n-2) + '*\n')*(n-3), end='')
    print('*'*n)

if __name__ == '__main__':
    cuadra(8)