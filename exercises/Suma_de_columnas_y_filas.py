matriz = [
    [10, 20, 30, 40],
    [50, 60, 70, 80],
    [90, 100, 200, 300],
]

n = len(matriz)
m = len(matriz[0])

sum_cols = []
sum_rows = []

for i in range(n):
    total = 0
    for j in range(m):
        total += matriz[i][j]
    sum_cols.append(str(total))

for j in range(m):
    total = 0
    for i in range(n):
        total += matriz[i][j]
    sum_rows.append(str(total))

print("La suma de las columnas es: {}".format(3))
print("La suma de las filas es: {}".format(" - ".join(sum_rows)))