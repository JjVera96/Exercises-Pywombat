import csv
import json

path = input('Ingresa la dirección del archivo .csv: ')

with open(path, 'r') as csv_file:
    with open(path.replace('.csv', '.json'), 'w') as json_file:
        reader =  csv.DictReader(csv_file)
        results = []
        for row in reader:
            results.append(dict(row))
        json.dump(results, json_file)
        
print('Archivo .json creado de forma exitosa.')