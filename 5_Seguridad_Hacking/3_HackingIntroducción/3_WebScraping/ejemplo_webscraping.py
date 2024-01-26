import requests
import re

url = "https://www.bodegaaurrera.com.mx/browse/tv-y-video/destacados-tv-y-video/destacados-pantallas/264711_300034_300035"

# <div class="mr1 mr2-xl b black green lh-copy f5 f4-l" aria-hidden="true">$7,990.00</div>
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'} # Simular que la petición se hace desde un navegador web
response = requests.get(url=url, headers=headers)

print(response.status_code)

if response.status_code == 200:
    print('Dentro')
    content = response.text
    regex = '<div class="mr1 mr2-xl b black green lh-copy f5 f4-l" aria-hidden="true">(.+?)</div>' # habiendo ubicado la etiqueta html donde se encuentra el precio de cada producto en el sitio se usa esa 
    # La expresión regular en este caso le dice al código que busque contenido en todos los div 
    for precio in re.findall(regex,content):
        print(f"El precio es: {precio[1: len(precio)]}") # Substring del string precio

else:
    print('No puedo hacer el proceso')
