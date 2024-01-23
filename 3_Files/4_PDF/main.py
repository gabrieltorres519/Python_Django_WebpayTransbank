from xhtml2pdf import pisa
from jinja2 import Template
import os
from datetime import datetime
import time

hoy = datetime.today()
timestamp = datetime.timestamp(hoy)
print(timestamp)
ruta = os.path.dirname(os.path.abspath(__file__))

sourceHtml = open(os.path.join(ruta, 'ejemplo.html')).read() # aqui ya no se utiliza ruta+'' porque la función join los usa como argumentos

print(sourceHtml)
print(type(sourceHtml))

# Ahora se parseará la salida que le vamos a dar a nuestro archivo pdf (darle un nombre)

# pdf = ruta + "/ejemplo.pdf"
pdf = f"{ruta}/pdf_{timestamp}.pdf" # Se genera el nombre del archivo con timestamp para saber exactamente cuándo se creó
print(pdf)

data = {"nombre": "Gabriel Torres", "ruta": ruta} # Los datos que está esperando el archivo html


# Ahora sí, la creación del archivo 

resutlFile = open(pdf, "w+b") # Los permisos son para leer el pdf y poder procesarlo

print(resutlFile)

# Configurar la implementación del template 

template = Template(open(os.path.join(ruta, "ejemplo.html")).read())

print(template)

html = template.render(data)
pisaStatus = pisa.CreatePDF(html,dest=resutlFile)

