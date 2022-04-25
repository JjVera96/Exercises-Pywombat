# https://pywombat.com/my/exercises/79a16057

class AbstrarObject:
    def __init__(self, kwargs):
        self.__dict__.update(kwargs)

if __name__ == '__main__':
    diccionario_user = {'username': 'Eduardo', 'password': 'Super password'}
    user = AbstrarObject(diccionario_user)
    print(user.username)
    print(user.password)