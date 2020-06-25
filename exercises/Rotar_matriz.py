def turn(matrix):
    rotated = []
    n = len(matrix)
    m = len(matrix[0])
    for j in range(m):
        row = []
        for i in range(n):
            row.append(matrix[i][j])
        rotated.append(row)
    return rotated

matrix = [ 
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(turn(matrix))

matrix = [ 
    [1, 2, 3, 4],
    [5, 6, 7, 8]
]

print(turn(matrix))