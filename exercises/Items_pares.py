if __name__ == '__main__':
    lista_a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    lista_a = [lista_a[i] for i in range(0, len(lista_a), 2)]
    # [1, 3, 5, 7, 9]
    print(lista_a)

    lista_b = [100, 78, 90, 5, 12, 134, 56, 78, 90, 9]
    lista_b = [lista_b[i] for i in range(0, len(lista_b), 2)]
    # [100, 90, 12, 56, 90]
    print(lista_b)
    
    lista_c = [80, 90, 100, 200, 300, 400, 500, 600]
    lista_c = [lista_c[i] for i in range(0, len(lista_c), 2)]
    # [80, 100, 300, 500]
    print(lista_c)
