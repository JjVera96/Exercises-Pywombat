import random 

l = [random.randint(0, 100) for i in range(50)]

for num in l:
    if(num > 50 and num%2 == 0): print(num)
