def common_keys(a: dict, b: dict):   
    keys_a = set(a.keys())
    keys_b = set(b.keys())
    return keys_a.intersection(keys_b)
    

a = {'a': 10, 'b':20, 'c':30}
b = {'a': 10, 'c': 30, 'd': 40}

print(common_keys(a, b))