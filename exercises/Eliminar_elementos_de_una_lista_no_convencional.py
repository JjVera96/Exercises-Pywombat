def remove_item(l, x):
    new_l = []
    for item in l:
        if item != x:
            new_l.append(item)
    return new_l
    
lista = ['uno', 'dos', 'tres', 'cuatro', 'cinco', 'seis', 'siete']

print(remove_item(lista, 'cinco'))