import requests
from bs4 import BeautifulSoup
import pandas 

URL = 'https://www.antipodas.net/coordenadaspais/'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
trs = soup.find_all('tr')
data = pandas.DataFrame(columns=['country', 'poblation', 'lng', 'lat'])

for tr in trs[1::]:
    tds = tr.find_all('td')
    country = tds[0].a.contents[0]
    lat, lng = tds[1].contents[0].split(' ')
    poblation = tds[2].contents[0]
    if poblation != 'N/S':
        poblation = int(poblation.replace('.', ''))
        data = data.append({'country': country, 'lat': lat, 'lng': lng, 'poblation': poblation}, ignore_index=True)
        
data = data.sort_values('poblation', ascending=False)
data.to_csv('antipodas.csv', index=False)