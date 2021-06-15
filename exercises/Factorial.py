def factorial(valor):
    if valor == 0 or valor == 1:
        return 1
    return valor * factorial(valor-1)

def factorial_iterativo(valor):
    if valor == 0 or valor == 1: return 1
    result = 1
    while(valor > 1): 
        result *= valor
        valor -= 1
    return result


print(factorial(3))
print(factorial_iterativo(3))
print(factorial(5))
print(factorial_iterativo(5))
print(factorial(15))
print(factorial_iterativo(15))