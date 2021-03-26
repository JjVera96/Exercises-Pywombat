n = int(input('Longitud de la lista: '))

l = []
for i in range(n):
    x = int(input('Ingresa un elemento: '))
    if x % 2 == 0:
        l.append(x)

for x in l:
    print(x)
