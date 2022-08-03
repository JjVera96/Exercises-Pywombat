#  https://pywombat.com/my/exercises/994d22da

import json 

if __name__ == '__main__': 
    obj = '{ "Name":"Eduardo", "Class":"User", "Age":28 }'
    dic = json.loads(obj)
    print(dic, type(dic))