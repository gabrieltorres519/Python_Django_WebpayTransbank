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
    password = '********' # Contraseña de aplicación creada en la cuenta que enviará el correo (en la sección verificación en dos pasos)
    toaddr = 'tgabinobeto2@gmail.com' # Cuenta a la que se enviará el correo
    
    asunto = "Aviso de pago BVVA"
    html = """ 
    <html>
        <head></head>
        <body>
            <h1>mensaje desde python con archivo adjunto</h1>
            <p>Hola qué tal cómo estás?</p>
        </body>
    </html>
    """

    # Configuración del mensaje
    msg = MIMEMultipart() # Objeto encargado de las configuraciones para el envío del mensaje
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = asunto
    msg.attach(MIMEText(html, 'html')) # Al constructor le mandamos el html y le indicamos que lo lea como html


    # Código para enviar archivo adjunto 
    filename = 'pdf_1706050646.029231.pdf'
    attachment = open(filename, "rb")
    part = MIMEBase('application', 'octet-stream') # Parametro application y el formato en el que se tiene que leer el archivo adjunto
    part.set_payload((attachment).read()) # Pasamos el archivo adjunto leído
    encoders.encode_base64(part)  # codificación del envió del correo
    part.add_header('Content-Disposition', "attachment; filename= %s" % filename)  # Agregando el encabezado y el archivo a enviar
    msg.attach(part) # Añadiendo el archivo adjunto al mensaje


    # Configuración del envío del correo 
    server = smtplib.SMTP('smtp.gmail.com', 587) # Nombre y puerto del servidor de correo
    server.starttls() # tls es el formato de renderización de los correos electrónicos, un forense de correos electrponicos apunta al tls, es como su firma
    server.login(fromaddr, password=password)
    
    # Configuración del cuerpo del correo
    text = msg.as_string()

    # Envío del correo
    server.sendmail(from_addr=fromaddr, to_addrs=toaddr, msg=text) 
    server.quit()


sendMail()