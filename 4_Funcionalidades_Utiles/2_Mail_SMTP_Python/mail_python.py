import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# Se recomienda crear una función para el envío de correos pues será 
# una funcionalidad que se usará de manera constante

# Se necesitará de una cuenta creada dentro de nuestro proveedor de hosting
# junto con nuestra contraseña 

# Solo para correos transaccionales, es decir, que generan directamente de 
# algún proceso de la aplicación y no para hacer mailmarketing

def sendMail():
    fromaddr = 'mailerdev6@gmail.com' # Cuenta que envia el correo
    password = '*****' # Contraseña de aplicación creada en la cuenta que enviará el correo (en la sección verificación en dos pasos)
    toaddr = 'tgabinobeto2@gmail.com' # Cuenta a la que se enviará el correo
    
    asunto = "Aviso de pago"
    html = """ 
    <html>
        <head></head>
        <body>
            <h1>mensaje desde python</h1>
            <p>Hola qué tal cómo estás?</p>
        </body>
    >/html>
    """

    # Configuración del mensaje
    msg = MIMEMultipart() # Objeto encargado de las configuraciones para el envío del mensaje
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = asunto
    msg.attach(MIMEText(html, 'html')) # Al constructor le mandamos el html y le indicamos que lo lea como html

    # Configuración del envío del correo 
    server = smtplib.SMTP('smtp.gmail.com', 587) # Nombre y puerto del servidor de correo
    server.starttls() # tls es el formato de renderización de los correos electrónicos, un forense de correos electrponicos apunta al tls, es como su firma
    server.login(fromaddr, password=password)

sendMail()