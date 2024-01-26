import requests
from bs4 import BeautifulSoup

url = "http://cesarcancino.com"
headers= {'User-Agent': 'Firefox'}
peticion = requests.get(url=url, headers=headers)
soup = BeautifulSoup(peticion.text, 'html.parser')
for enlace in soup.find_all('link'):
    if ('/wp-content/themes') in enlace.get('href'):
        the = enlace.get('href')
        the=the.split('/')
        if 'themes' in the:
            pos = the.index('themes')
            theme =the[pos+1]
            print(theme) # Se imprimen los temas instalados en el sitio wordpress

# Los temas es solo una de las informaciones que podemos obtener de un sitio wordpress