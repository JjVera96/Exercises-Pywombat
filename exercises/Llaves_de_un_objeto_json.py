# https://pywombat.com/my/exercises/279e0d6e

import json

def main():
    with open('./resources/users.json', 'r') as f:
        data = json.load(f)

    for user in data['users']:
        print(user['nombre'])


if __name__ == '__main__':
    main()