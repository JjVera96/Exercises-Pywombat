def last_elements(l, index):
    return tuple(l[-index::])

print(last_elements([1, 2, 3, 4, 5, 6 ],  2))
print(last_elements([True, True, False, False, True ],  3))
print(last_elements(['PyWombat', 'Article', 'Ben'],  1))
