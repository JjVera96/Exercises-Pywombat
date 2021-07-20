from random import randint

if __name__ == '__main__':
    n = 10                                               # 1
    vector = [randint(0, 2*n) for _ in range(1, n+1)]    # n
    print(vector)                                          
    sumatoria = sum(vector)                              # n
    promedio = sumatoria/n                               # 1
    print(promedio)
    result = []
    for data in vector:
        if data > promedio: result.append(data)          # n
    print(result)

