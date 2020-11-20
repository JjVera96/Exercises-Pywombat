def happy_number(number):
    if(number<0):
        return False
    trace = []
    while(number != 1 and not number in trace):
        trace.append(number)
        result = 0
        for digit in str(number): result += int(digit) ** 2
        number = result
    return number == 1
    
print(happy_number(7))
print(happy_number(19))
print(happy_number(5))