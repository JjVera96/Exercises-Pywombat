# https://pywombat.com/my/exercises/9133f0a9

def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i-1
        while(j >= 0 and arr[j] > key):
            arr[j+1] = arr[j]
            j = j-1
        arr[j+1] = key
    return arr

if __name__ == '__main__':
    arr = insertion_sort([10, 2, 1, 2, 4, 5, 7, 9])
    print(arr)
