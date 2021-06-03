def mcm(a, b):
    if a < b:
        num1 = a
        num2 = b
    else:
        num1 = b
        num2 = a 
    for i in range(num2, 0, -1):
        if num2 % i == 0 and num1 % i == 0:
            mcd = i
            break
    return (num1 * num2) // mcd
        

print(mcm(4, 17))