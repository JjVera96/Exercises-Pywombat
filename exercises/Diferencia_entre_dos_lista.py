def array_diff(a, b):
    diff_ab = set(a) - set(b)    
    diff_ba = set(b) - set(a)
    return list(diff_ab.union(diff_ba))

if __name__ == '__main__':
    print(array_diff([1], [1, 2, 3, 2]))
    print(array_diff([1, 2, 3, 2], [1]))
    print(array_diff([1, 4, 3, 5], [1, 2, 3, 2]))
