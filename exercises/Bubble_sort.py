def burbuja(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                aux = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = aux
    return arr

if __name__ == '__main__':
    lista_a = [10, 22, 1, 3, 60, 87, 10, 34, 1, 2, 1, 56, 78]
    print(burbuja(lista_a))

    lista_b = [5, 10, 78, 34, 12, 156, 78, 543, 1900, 183, 3, 4]
    print(burbuja(lista_b))
