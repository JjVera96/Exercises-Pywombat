import json 

name = input("Nombre: ")
email = input("Email: ")
age = input("Edad: ")
postal_code = input("Código Postal: ")


data = {
    "name": name,
    "email": email,
    "age": age,
    "postal_code": postal_code
}

with open('../resources/user.json', 'w') as outfile:
    json.dump(data, outfile)
    
print("Archivo .json creado exitosamente.")