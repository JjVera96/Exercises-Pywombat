import hashlib

class User():
    def __init__(self, password):
        self._password = hashlib.sha512(password.encode('utf-8')).hexdigest()
        
    def change_password(self, password):
        self._password = hashlib.sha512(password.encode('utf-8')).hexdigest()
        
    @property
    def password(self):
        return self._password
        
user = User('password123')
print(user.password)
user.change_password('change_password123')
print(user.password)