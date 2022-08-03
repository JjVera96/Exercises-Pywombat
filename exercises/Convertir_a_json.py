# https://pywombat.com/my/exercises/a7caba9f

import json

python_obj = {
  "nomnre": "Eduardo",
  "edad": 27
}

json_text = json.dumps(python_obj)

print(json_text)