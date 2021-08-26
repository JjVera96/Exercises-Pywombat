import json

if __name__ == '__main__':
    file = open('resources/user.json', 'r')
    data = json.load(file)
    for user in data['users']:
        print(user)
