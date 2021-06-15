def simple_list(_list):
    return list(set(_list))

if __name__ == '__main__':
    lista_a = [1, 2, 3, 2, 10, 20, 10, 2, 3, 4, 5, 2, 2] 
    print(simple_list(lista_a))
    [1, 2, 3, 10, 20, 4, 5]

    lista_b = [110, 20, 45, 50] 
    print(simple_list(lista_b))
    [110, 20, 45, 50] 

    lista_c = [1, 2, 3, 4, 4, 4, 4, 4, 4, 4, 4] 
    print(simple_list(lista_c))
