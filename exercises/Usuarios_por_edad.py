# https://pywombat.com/my/exercises/867900f8

if __name__ == '__main__':
    users = [
        {'username':  'Eduardo', 'age': 27 },
        {'username':  'Fernando', 'age': 25 },
        {'username':  'Loki', 'age': 30 },
        {'username':  'Duke', 'age': 19}
    ]

    for user in users:
        if user.get('age', 0) > 25:
            print(user['username'])
