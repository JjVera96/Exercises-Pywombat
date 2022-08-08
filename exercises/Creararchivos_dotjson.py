# https://pywombat.com/my/exercises/c047b6e3

import json 

def main():
    users = [
        {
            "nombre": "Eduardo",
            "edad": 27
        },
        {
            "nombre": "Raquel",
            "edad": 29
        },
        {
            "nombre": "Fernando",
            "edad": 25
        },
        {
            "nombre": "Guadalupe",
            "edad": 30
        }
    ]

    with open('./resources/users-out.json', 'w') as f:
        json.dump(users, f, indent=4)

if __name__ == '__main__':  
    main()