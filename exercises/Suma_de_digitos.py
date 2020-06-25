def sum_digits(number):
    return sum(list(map(lambda x: int(x), str(number))))
    
print(sum_digits2(10))
print(sum_digits2(1234))