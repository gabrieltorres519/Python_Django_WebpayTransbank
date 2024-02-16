from datetime import datetime, date, timedelta

from django.conf import settings
import os
from os import remove
from urllib.parse import urlparse, parse_qs
from django.core.paginator import Paginator
from django.template import Context, Template
#token
import jwt
import time
#email
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from smtplib import SMTPResponseException


def getToken(json):
    token= jwt.encode(json, settings.SECRET_KEY, algorithm='HS256')
    return token


def traducirToken(token):
    return jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])


def sendMail(html, asunto, para):

    fromaddr = settings.MAIL_SALIDA # Cuenta que envia el correo
    password = settings.PASSWORD_MAIL_SALIDA # Contraseña de aplicación creada en la cuenta que enviará el correo (en la sección verificación en dos pasos)
    toaddr = para # Cuenta a la que se enviará el correo
    

    # Configuración del mensaje
    msg = MIMEMultipart() # Objeto encargado de las configuraciones para el envío del mensaje
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = asunto
    msg.attach(MIMEText(html, 'html')) # Al constructor le mandamos el html y le indicamos que lo lea como html


    # Configuración del envío del correo 
    server = smtplib.SMTP(settings.SERVER_STMP, settings.PUERTO_SMTP) # Nombre y puerto del servidor de correo
    server.starttls() # tls es el formato de renderización de los correos electrónicos, un forense de correos electrponicos apunta al tls, es como su firma
    server.login(fromaddr, password=password)
    
    # Configuración del cuerpo del correo
    text = msg.as_string()

    # Envío del correo
    server.sendmail(from_addr=fromaddr, to_addrs=toaddr, msg=text) 
    server.quit()


def getExtension(file):
    extension = os.path.splitext(str(file))[1]
    if extension == ".png":
        return True
    elif extension == ".jpg":
        return True
    elif extension == ".jpeg":
        return True
    elif extension == ".JPG":
        return True
    elif extension == ".PNG":
        return True
    elif extension == ".JPEG":
        return True
    else:
        return False


def paginacion(total, request):
    paginator = Paginator(total, settings.TOTAL_PAGINAS)
    page = request.GET.get('page')
    datos = paginator.get_page(page)
    numeros=[]
    if len(datos)>=settings.TOTAL_PAGINAS:
        for ultima in range(1, datos.paginator.num_pages):
            numeros.append(ultima)
        numeros.append(ultima+1)
    return [datos, numeros, page]


def numberFormat(numero):
    if numero == None:
        return 0
    else:
        return "{:,}".format(numero).replace(",",".")