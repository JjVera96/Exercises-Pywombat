def get_min(dictionary):
    return min(dictionary.items(), key=lambda x: x[1])[0]

d = {'a': 10, 'b': 5, 'c': 50, 'd': 180, 'e': 1, 'f': 150 }
print(get_min(d))

d = {'a': 11 , 'b': 65, 'c':  80, 'd': 9, 'e': -1, 'f': -150 }
print(get_min(d))