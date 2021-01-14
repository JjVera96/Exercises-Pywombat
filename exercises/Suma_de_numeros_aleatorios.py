import random 

n = int(input("Cantidad de números aleatorios a generar: "))

sum_n = 0
for i in range(n): 
    sum_n += random.randint(1,100)
    
print("El resultado de la suma: {}".format(sum_n))