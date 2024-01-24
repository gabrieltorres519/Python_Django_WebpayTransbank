# pip install jwt
# pip install PyJWT
# pip install python-jose

# Llamamos al archivo diferente de jwt debido a que nos dará error de que no existe algún atributo en 
# jwt si le dejamos ese nombre genérico (el mismo que la librería instalada)

import jwt 
import time

secreto = "123456"

ts = int(time.time())
print(ts)

payload = {'id':1, 'nombre':'Gabriel Torres', 'time': ts}

token = jwt.encode(payload, secreto, algorithm='HS256') # Creamos el token codificado

print(token)

resuelto = jwt.decode(token, secreto, algorithms=["HS256"]) # Decodificamos con el algoritmo más utilizado

print(f"Token = {token} | Resuelto = {resuelto}")