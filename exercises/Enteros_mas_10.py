# https://pywombat.com/my/exercises/2de24a74

def consecutivos(arr):
    for i in range(len(arr) - 1):
        if arr[i] != arr[i+1] - 10: return False
    return True

if __name__ == '__main__':
    listado = [10, 20, 30, 40, 50, 60]
    print(consecutivos(listado))

    listado = [10, 20, 30, 40, 50, 60, 65]
    print(consecutivos(listado))

    listado = [1, 11, 21, 31, 41, 51]
    print(consecutivos(listado))

    listado = [-20, -10, 0, 10, 20 ]
    print(consecutivos(listado))
