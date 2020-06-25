import requests
import pymongo 
import pprint


username = 'username'
gender = 'gender'
name = 'name'
age = 'age'
email = 'email'
address = 'address'
city = 'city'
state = 'state'
contry = 'contry'
postcode = 'postcode'

usuarios = [{
        username: 'user1',
        gender: 'female',
        name: 'Katie Chavez',
        age: 26,
        email: 'user1@blueproject.com',
        address: {
            city: 'Aberdeen',
            state: 'Lothian',
            contry: 'United Kingdom'
        }
    },{
        username: 'user2',
        gender: 'male',
        name: 'Konstantinos Dahlke',
        age: 37,
        email: 'user2@blueproject.com',
        address: {
            city: 'Bad Nauheim',
            state: 'Baden-Württemberg',
            contry: 'Germany'
        }
    },{
        username: 'user3',
        gender: 'female',
        name: 'Scarlett Wilson',
        age: 57,
        email: 'user3@blueproject.com',
        address: {
            city: 'Taupo',
            state: 'Marlborough',
            contry: 'New Zealand'
        }
    },{
        username: 'user4',
        gender: 'male',
        name: 'David Harris',
        age: 57,
        email: 'user4@blueproject.com',
        address: {
            city: 'Gisborne',
            state: 'Manawatu-Wanganui',
            contry: 'New Zealand'
        }
    },{
        username: 'user5',
        gender: 'female',
        name: 'June Wallace',
        age: 28,
        email: 'user5@blueproject.com',
        address: {
            city: 'Indianapolis',
            state: 'Vermont',
            contry: 'United States'
        }
    },{
        username: 'user6',
        gender: 'female',
        name: 'Catalina Marin',
        age: 24,
        email: 'user6@example.com',
        address: {
            city: 'Torrejón de Ardoz',
            state: 'Castilla la Mancha',
            contry: 'Spain'
        }
    },{
        username: 'user7',
        gender: 'male',
        name: 'Rochus Lipinski',
        age: 75,
        email: 'user7@example.com',
        address: {
            city: 'Steinach',
            state: 'Nordrhein-Westfalen',
            contry: 'Germany'
        }
    },{
        username: 'user8',
        gender: 'female',
        name: 'Josefina Denis',
        age: 68,
        email: 'user8@example.com',
        address: {
            city: 'Weesen',
            state: 'Bern',
            contry: 'Switzerland'
        }
    },{
        username: 'user9',
        gender: 'female',
        name: 'Larissa Runge',
        age: 37,
        email: 'user9@blueproject.com',
        address: {
            city: 'Neudenau',
            state: 'Saarland',
            contry: 'Germany',
            postcode: 56191
        }
    },{
        username: 'user10',
        gender: 'female',
        name: 'Shannon Moore',
        age: 14,
        email: 'user10@blueproject.com',
        address: {
            city: 'Queanbeyan',
            state: 'Australian Capital Territory',
            contry: 'Australia',
            postcode: 7577
        }
    }]

client = pymongo.MongoClient("mongodb+srv://admin:admin@test-oauly.gcp.mongodb.net/test?retryWrites=true&w=majority")
db = client.test

# Agregar los usuarios
#db.usuarios.insert_many(usuarios)

# Contar los usuarios
print('\nContar los usuarios')
print(db.usuarios.count_documents({}))

# Filtrar los usuarios con edad mayor de 25
print('\nFiltrar los usuarios con edad mayor de 25')
for user in db.usuarios.find({'age': {'$gt': 25}}):
    pprint.pprint(user)

# Promedio de los usuarios 
print('\nPromedio de los usuarios ')
for result in db.usuarios.aggregate([{'$group': {'_id': '$tags', 'avg': {'$avg': '$age'}}}]):
    pprint.pprint(result)
    
# Promedio de los usuarios con email terminado blueproject.com.
print('\nPromedio de los usuarios con email terminado blueproject.com.')
for result in db.usuarios.aggregate([
    {'$match': {'email': {'$regex': '[\w+]@blueproject.com'}}},
    {'$group' : {'_id' : None, 'avg': {'$avg': '$age' }}}]):
    pprint.pprint(result)
    
# Listas todos los usuarios con correo example.com
print('\nListas todos los usuarios con correo example.com')
for result in db.usuarios.find({'email': {'$regex': '[\w+]@example.com'}}):
    pprint.pprint(result)

# Obtener la cantidad de usuarios con correo example.com
print('\nObtener la cantidad de usuarios con correo example.com')
for result in db.usuarios.aggregate([
    {'$match': {'email': {'$regex': '[\w+]@example.com'}}},
    {'$count' : 'count'}]):
    pprint.pprint(result)
    
# Obtener todos los usuarios que actualmente vivan en el país Germany (Alemania).
print('\nObtener todos los usuarios que actualmente vivan en el país Germany (Alemania).')
for result in db.usuarios.find({'address.contry': 'Germany'}):
    pprint.pprint(result)
    
# Obtener todos los usuarios que posean código postal.
print('\nObtener todos los usuarios que posean código postal.')
for result in db.usuarios.find({'address.postcode': {'$exists': True}}):
    pprint.pprint(result)

# Obtener la cantidad de hombres dentro de la colección.
print('\nObtener la cantidad de hombres dentro de la colección.')
for result in db.usuarios.aggregate([{'$match': {'gender': 'male'}},{'$count' : 'count'}]):
    pprint.pprint(result)

# Obtener la cantidad de mujeres dentro de la colección.
print('\nObtener la cantidad de mujeres dentro de la colección.')
for result in db.usuarios.aggregate([{'$match': {'gender': 'female'}},{'$count' : 'count'}]):
    pprint.pprint(result)

# Obtener la cantidad de mujeres que viven en Germany (Alemania).
print('\nObtener la cantidad de mujeres que viven en Germany (Alemania).')
for result in db.usuarios.aggregate([{'$match': {'gender': 'female', 'address.contry': 'Germany'}},{'$count' : 'count'}]):
    pprint.pprint(result)
    
# Obtener el nombre completo del usuario más joven.
print('\nObtener el nombre completo del usuario más joven.')
for result in db.usuarios.aggregate([{'$sort': {'age': 1}},{'$limit' : 1}, {'$project': {'username': 1, '_id': 0} }]):
    pprint.pprint(result)