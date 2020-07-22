matriz = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 100],
]

fils = []
cols = []
sum_esquinas = matriz[0][0] + matriz[0][-1] + matriz[-1][0] + matriz[-1][-1]

for x in range(3):
    fils.append(sum(matriz[x]))
    cols.append(matriz[0][x] + matriz[1][x] + matriz[2][x])
    
print("La suma de las filas es: {} - {} - {}".format(fils[0], fils[1], fils[2]))
print("La suma de las columnas es: {} - {} - {}".format(cols[0], cols[1], cols[2]))
print("La suma de las esquinas es:", sum_esquinas)
    