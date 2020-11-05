users = [
    { 'name': 'Luis', 'age': 27 },
    { 'name': 'Raquel', 'age': 13 },
    { 'name': 'Eduardo', 'age': 35 },
    { 'name': 'Fernando', 'age': 12},
    { 'name': 'Esmeralda', 'age': 45 },
    { 'name': 'Sophie', 'age': 9}
]

users = sorted(users, key=lambda x: x['age'])
for user in users[0:3]: print(user['name'])