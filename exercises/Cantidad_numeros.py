def cantidad_digitos(num):
    cant = 0
    while(num>0):
        cant += 1
        num = num // 10
    return cant

print(cantidad_digitos(0))
print(cantidad_digitos(10))
print(cantidad_digitos(2019))
print(cantidad_digitos(1234567890))