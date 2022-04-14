# https://pywombat.com/my/exercises/dd9910f3

import json

if __name__ == '__main__':
    data = {'Name': 'Eduardo', 'Class': 'User', 'Age': 28}
    with open('../resources/user.json', 'w') as outfile:
        json.dump(data, outfile)
