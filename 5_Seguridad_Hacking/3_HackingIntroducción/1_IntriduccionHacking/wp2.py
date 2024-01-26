import requests
from bs4 import BeautifulSoup

url = "http://cesarcancino.com"
headers= {'User-Agent': 'Firefox'}
peticion = requests.get(url=url, headers=headers)
soup = BeautifulSoup(peticion.text, 'html.parser')
for v in soup.find_all('meta'):
    if v.get('name') == 'generator':
        version = v.get('content')
        print(version) # Obteniendo la versión de wordpress
