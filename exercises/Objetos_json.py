# https://pywombat.com/my/exercises/c49d40cb

import json

if __name__ == '__main__':
    sjson = '{"nombre": "Eduardo", "edad": 27}'
    jjson = json.loads(sjson)
    print(jjson)
