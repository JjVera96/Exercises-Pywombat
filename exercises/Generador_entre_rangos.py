def pares(n, m):
    nums = []
    if n > m or n <= 0 or m <= 0:
        raise Exception("No es posible continuar con la operación.")
    n = n if n % 2 == 0 else n + 1
    for num in range(n, m, 2):
        nums.append(num)
    return nums
    

print(pares(5, 10))
print(pares(15, 10))
    
        