"""
numbers = range(0, 10)
evens = []
for number in numbers:
    if number % 2 == 0:
        evens.append(number)
"""

evens = [ number for number in range(0, 10) if number % 2 == 0]
print(evens)