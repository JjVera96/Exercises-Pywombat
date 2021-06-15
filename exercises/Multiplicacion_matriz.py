matrix_a = [ 
    [1, 2, 3],
    [4, 5, 6]
]

matrix_b = [ 
    [1, 2, 3, 4],
    [4, 5, 6, 7],
    [7, 8, 9, 10]
]


def multiplicacion_matriz(a, b):
    result = []
    for i in range(len(a)):
        line = []
        for j in range(len(b[0])):
            sum = 0
            for k in range(len(b)):
                sum += a[i][k] * b[k][j] 
            line.append(sum)
        result.append(line)
    return result
        

print(multiplicacion_matriz(matrix_a, matrix_b))