# https://pywombat.com/my/exercises/be6f1808

def selection_sort(arr):
    for i in range(len(arr)-1):
        min = i
        for j in range(i, len(arr)):
            if arr[j] < arr[min]:
                min = j
        aux = arr[i]
        arr[i] = arr[min]
        arr[min] = aux
    return arr

if __name__ == '__main__':
    arr = [1,2,3,4,5,6,7, 8, 9, 10]
    print(selection_sort(arr))

    arr = [2,1,3,5,5,6,71, 81, 9, 10]
    print(selection_sort(arr))

    arr = [111,22,13,74,305,36,67,18, 9, 10]
    print(selection_sort(arr))