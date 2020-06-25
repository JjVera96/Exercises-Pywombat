l = []

for i in range(10):
    nota = input('Ingresa una calificación: ')
    l.append(int(nota))

print('El promedio es: ', sum(l)/len(l))