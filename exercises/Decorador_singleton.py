def singleton(cls):
    instances = dict()

    def wrapper(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return wrapper
    

@singleton
class User:
    def __init__(self, username):
        print('Nueva instancia!')
        self.username = username

user1 = User("Username1")
user2 = User("Username2")
user3 = User("Username3")
