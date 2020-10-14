def thanosSort(l):
    return len(l) if sorted(l) == l else thanosSort(l[:len(l)//2])

print(thanosSort([1, 2, 2, 4]))
print(thanosSort([11, 12, 1, 2, 13, 14, 3, 4]))
print(thanosSort([7, 6, 5, 4]))
        