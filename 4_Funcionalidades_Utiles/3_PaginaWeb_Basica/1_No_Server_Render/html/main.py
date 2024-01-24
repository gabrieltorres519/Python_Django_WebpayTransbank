from  jinja2 import FileSystemLoader, Environment
from wsgiref.simple_server import make_server
import os # Para buscar el nombre del archivo con el que se trabajará

def desplegar(environ, start_response): # Environ configurará los datos del servidor y lo hará correr, start_response va a recibir el formato de la petición y 
                                        # la parametrización de la respuesta con la que vamos a trabajar 
    ruta = os.path.dirname(os.path.abspath(__file__))
    env = Environment(loader=FileSystemLoader(ruta+'/templates')) # Para buscar los archivos html en el ambiente virtual, los tenemos en la carpeta templates que creamos
    template = env.get_template('template.html')

    data = {
        'titulo': "Hola mundo"
    }
    html = template.render(data) 
    headers = [('Content-type','text/html; charset=utf-8')]
    
    start_response('200 OK', headers)

    return [bytes(html,'utf-8')]

# Ojo que todo lo que sea recurso, como las imágenes, se tienen que configurar sus 
# rutas en la configuración del server, pero es mejor alojarlas en un servicio y solo usar
# sus urls en el archivo html

server = make_server('localhost', 8003, desplegar) # Localhost se cambiaría por el dominio en donde se aloja la página y 8003 es el puerto
server.serve_forever()
