from copy import deepcopy

list_a = [3, [55, 44], (7, 8, 9)]
list_b = deepcopy(list_a)

print(list_a is list_b)
print(list_a == list_b)

