# https://pywombat.com/my/exercises/e308935f

def buble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                aux = arr[j]
                arr[j]= arr[j+1]
                arr[j+1]= aux
    return arr

if __name__ == '__main__':
    arr = buble_sort([10, 2, 1, 2, 4, 5, 7, 9])
    print(arr)