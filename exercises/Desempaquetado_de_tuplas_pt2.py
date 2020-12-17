t = ('Loki', 'Duke', 'Princesa', 'Lisa', 'Burns', 'Latin')
n = len(t)

for index, element in enumerate(t):
    if index == 0: print("Primer elemento ", element)
    if index == 1: print("Segundo elemento ", element)
    if index == n-1: print("Ultimo elemento ", element)