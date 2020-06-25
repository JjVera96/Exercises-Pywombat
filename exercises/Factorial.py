def factorial(valor):
    if valor == 0 or valor == 1:
        return 1
    return valor * factorial(valor-1)

print(factorial(3))
print(factorial(5))
print(factorial(15))