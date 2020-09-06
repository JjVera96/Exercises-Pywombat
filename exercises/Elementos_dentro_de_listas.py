def sub_list(list_x, list_y):
    list_z = []
    if len(list_x)>len(list_y): return list_z
    for param in list_x:
        if param in list_y: list_z.append(param)
    return list_z

        
print(sub_list( [1, 2, 3, 4, 5],  [0, 2, 4, 6, 8, 10] ))
print(sub_list( [6, 7, 1, 2, 1, 3, 4, 5], [7, 8, 1, 3, 2, 1, 7, 3,7, 10] ))
print(sub_list( [0, 2, 4, 6, 8, 10], [1, 2, 3, 4, 5] ))