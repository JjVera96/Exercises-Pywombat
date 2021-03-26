import requests
import pandas

response = requests.get('https://randomuser.me/api/?results=100').json()
# print(response)

titles = ['nombre_completo', 'edad', 'genero', 'correo_electronico', 'pais', 'codigo_postal']


def user_format(user):
    return {
     'nombre_completo': ' '.join(user['name'].values()),
     'edad': user['dob']['age'],
     'genero': user['gender'],
     'correo_electronico': user['email'],
     'pais': user['location']['country'],
     'codigo_postal': user['location']['postcode']
    }

users = list(map(lambda user: user_format(user), response['results']))
df = pandas.DataFrame(users, columns=titles)
df.to_csv('../resources/users.csv', index=False)
