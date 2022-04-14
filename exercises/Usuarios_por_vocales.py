# https://pywombat.com/my/exercises/6a979cab

if __name__ == '__main__':
    usuarios = [
        {'username':  'Eduardo', 'age': 27 },
        {'username':  'Fernando', 'age': 25 },
        {'username':  'Loki', 'age': 30 },
        {'username':  'Duke', 'age': 19}
    ]

    for usuario in usuarios: 
        if usuario.get('username')[0] in 'aeiouAEIOU': 
            print(usuario.get('username'))
        