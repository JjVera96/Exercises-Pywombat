num_1 = int(input("Introduce tu primer número: "))
num_2 = int(input("Introduce tu segundo número: "))
num_3 = int(input("Introduce tu tercer número: "))

list_num = sorted([num_1, num_2, num_3], reverse=True)
print("El orden es: {} - {} - {}".format(list_num[0], list_num[1], list_num[2]))