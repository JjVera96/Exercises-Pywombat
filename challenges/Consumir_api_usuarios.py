import requests
import xlsxwriter

response = requests.get('https://randomuser.me/api/?results=100').json()
response['results'].sort(key=lambda usuario: usuario['dob']['age'], reverse=True)

workbook = xlsxwriter.Workbook('usuarios.xlsx')
worksheet = workbook.add_worksheet('Lista')

col = row = 0
titles = ['Genero','Nombre Completo', 'Email', 'Edad']
for i in range(len(titles)):
    worksheet.write(row, col+i, titles[i])

row += 1

for usuario in response['results']:
    worksheet.write(row, col, usuario['gender'])
    worksheet.write(row, col+1, ' '.join(usuario['name'].values()))
    worksheet.write(row, col+2, usuario['email'])
    worksheet.write(row, col+3, usuario['dob']['age'])
    row += 1
    
workbook.close()