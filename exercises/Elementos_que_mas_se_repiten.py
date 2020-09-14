cant = int(input("Cantidad de elementos: "))
nums = []
num_repeat = None
cant_repeat = None

for i in range(cant):
    num = int(input("Ingresa el {}º número: ".format(i+1)))
    nums.append(num)
    if nums.count(num) > 1:
        if cant_repeat is None or cant_repeat < nums.count(num):
            cant_repeat = nums.count(num) 
            num_repeat = num
            
if cant_repeat:
    print("El número que más se repite es: {}".format(num_repeat))
else:
    print("Todos los elementos son únicos en tu lista")