# https://pywombat.com/my/exercises/ca8378fe

import json

if __name__ == '__main__':
    obj = {'Name': 'Eduardo', 'Class': 'User', 'Age': 28}

    print(json.dumps(obj, sort_keys=True, indent=4))