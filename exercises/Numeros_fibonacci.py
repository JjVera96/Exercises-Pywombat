def fibonacci(maxnumber):
    l = []
    suma = 0
    num = 1
    if(maxnumber > 0):
        for _ in range(maxnumber):
            l.append(suma)
            suma, num = num, suma+num
    return l


def fibonacci_v2(maxnumber):
    suma = 0
    num = 1
    if(maxnumber > 0):
        for _ in range(maxnumber):
            suma, num = num, suma+num
    return suma
    
print(fibonacci(1))
print(fibonacci_v2(1))
print(fibonacci(3))
print(fibonacci_v2(3))
print(fibonacci(12))
print(fibonacci_v2(12))
