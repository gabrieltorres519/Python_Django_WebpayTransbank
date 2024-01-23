import requests

endpoint = "http://localhost/clientes"

r = requests.get('https://httpbin.org/basic-auth/user/pass', auth=('user', 'pass'))
print(r.status_code)
print(r.headers['content-type'])
print(r.encoding)
print(r.text)
print(r.json())

# documentación para hacer hits a enpoints con la librería requests https://requests.readthedocs.io/en/latest/ 
