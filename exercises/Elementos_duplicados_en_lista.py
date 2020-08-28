def items_duplicate(sequence):
    while(len(sequence)):
        number = sequence[0]
        cant_number = sequence.count(number)
        if(cant_number > 1): print('El número {} se encuentra repetido {} veces'.format(number, cant_number))
        for i in range(cant_number): sequence.remove(number)
        
items_duplicate([1, 2, 3, 4, 5, 5])
items_duplicate([10, 10, 20, 30, 10, 10, 20, 50, 60, 10, 20])