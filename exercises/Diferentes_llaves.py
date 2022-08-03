# https://pywombat.com/my/exercises/9d18b884

if __name__ == '__main__':
    dict_a = {'a': 10, 'b': 20, 'c': 30, 'd': 40, 'e': 50}
    dict_b = {'a': 10, 'b': 20, 'f': 60, 'g': 70, 'h': 80}
    keys_a = set(dict_a.keys())
    keys_b = set(dict_b.keys())
    result = keys_a.symmetric_difference(keys_b)
    print(result)



