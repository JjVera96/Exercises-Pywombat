# https://pywombat.com/my/exercises/b6bc6446

import operator

if __name__ == '__main__':
    usuarios = [
        {'name': 'user1', 'age': 27},
        {'name': 'user2', 'age': 12},
        {'name': 'user3', 'age': 10},
        {'name': 'user4', 'age': 36},
        {'name': 'user5', 'age': 12},
    ]

    users_sorted = sorted(usuarios, key=operator.itemgetter('age'))
    print(users_sorted)

