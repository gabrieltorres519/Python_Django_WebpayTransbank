import requests

obj = requests.get("http://cesarcancino.com")
headers = dict(obj.headers)
print(headers)

# Se recibirá un diccionario con las cabeceras del sitio web 

"""
python3 test2.
py
{'Date': 'Thu, 25 Jan 2024 23:23:06 GMT', 'Server': 'Apache', 'Link': '<https://www.cesarcancino.com/wp-json/>; rel="https://api.w.org/", 
<https://www.cesarcancino.com/wp-json/wp/v2/pages/9>; rel="alternate"; type="application/json", <https://www.cesarcancino.com/>; rel=shortlink',
 'Upgrade': 'h2', 'Connection': 'Upgrade, Keep-Alive', 'Cache-Control': 'max-age=600', 'Expires': 'Thu, 25 Jan 2024 23:33:06 GMT', 
 'Vary': 'Accept-Encoding,User-Agent', 'Content-Encoding': 'gzip', 'Content-Length': '6227', 'Keep-Alive': 'timeout=5, max=100', 
 'Content-Type': 'text/html; charset=UTF-8'}
"""

