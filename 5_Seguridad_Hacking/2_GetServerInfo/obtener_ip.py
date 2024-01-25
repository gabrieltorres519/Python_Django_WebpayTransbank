# Para obtener la dirección ip de la terminal en la que estás trabajando, puede ser la terminal de un servidor remoto en
# el que estás trabajando


import socket
import urllib.request

servidor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 

 # Red con formato, para saber cuál es la red en la que estámos parados 
servidor.connect(('8.8.8.8', 80)) # 

print(f"La ip del servidor es {servidor.getsockname()[0]}")

print(f"Nombre del equipo es {socket.gethostbyname(socket.gethostname())} | {socket.gethostname()}")

servidor.close()