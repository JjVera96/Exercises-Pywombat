def rango_pares(x, y):
    if x > y: x, y = y, x
    x = x+1 if(x%2) else x
    l = []
    for i in range(x, y, 2):
        l.append(i)
    return l

x = int(input("Ingrese x: "))
y = int(input("Ingrese y: "))
print(rango_pares(x, y))

