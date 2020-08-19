def tipos(x, y):
    if type(x) == list and type(y) == list:
        print('Ambos objetos son listas')
    else:
        print('No son objetos listas')
        
tipos([1, 2, 3], (1, 2 , 3))
tipos([1, 2, 3], [1, 2 , 3])
