my_dict = {'a': 'String', 'b': 10,  'c': 3.14, 'd': False, 'e': [1, 2, 3], 'f': (4, 5, 6)}

key = input("Ingresa una llave: ")

if key in my_dict:
    print(my_dict[key])
else:
    print("Lo sentimos, la llave ingresada no se encuentra en el diccionario.")
