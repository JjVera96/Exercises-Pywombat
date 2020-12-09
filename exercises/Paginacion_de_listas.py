list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def paginate(list, page=1, per_page=10):
    return list[page: page+per_page if page+per_page < len(list) else len(list)-1 ]

print(paginate(list, 2, 2))
print(paginate(list, 3, 2))
print(paginate(list, 1, 5))
print(paginate(list, 2, 5))