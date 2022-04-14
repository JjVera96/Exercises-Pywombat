# https://pywombat.com/my/exercises/3d4319df

if __name__ == '__main__':
    n = 5
    flat = True
    for i in range(2*n):
        if i > n: flat = False
        k = i if flat else 2*n-i
        for j in range(k):
            print('* ', end=' ')
        print('')
