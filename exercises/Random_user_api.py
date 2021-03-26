import requests
import pandas

df = pandas.DataFrame(columns=['name', 'age', 'gender', 'email', 'country', 'postal_code'])

response = requests.get('https://randomuser.me/api?results=500').json()

for user in response['results']:
    row = {}
    row['name'] = ' '.join(user['name'].values())
    row['age'] = user['dob']['age']
    row['gender'] = user['gender']
    row['email'] = user['email']
    row['country'] = user['location']['country']
    row['postal_code'] = user['location']['postcode']
    df = df.append(row, ignore_index=True)

df = df.drop_duplicates(subset=['name', 'email'])
df.to_csv('user.csv', index=False)
