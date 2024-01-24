from jose import jwt 
import time

secreto = "123456"

ts = int(time.time())

payload = {'id':1, 'nombre':'Gabriel Torres', 'time': ts}

token = jwt.encode(payload, secreto, algorithm='HS256') # Creamos el token codificado

print(token)

resuelto = jwt.decode(token, secreto, algorithms=["HS256"])

print(f"Token = {token} | Resuelto = {resuelto}")

