import smtplib
import os
from dotenv import load_dotenv
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.message import MIMEMessage

# Upload eviroments variables from .env archive
load_dotenv()

remitente = os.getenv('USER')
destinatario = os.getenv('USER')
asunto = "Test"

msg = MIMEMultipart()
msg['From'] = remitente
msg['To'] = destinatario
msg['Subject'] = asunto

with open('C:/Users/HP/OneDrive/Escritorio/Desarrollo/Back-End/send_email/send_email_youtube/templates/index.html', 'r') as archive:
    contenido = archive.read()
    # body = MIMEText(archive.read(), 'html')

# Adjuntar el contenido html
# msg.attach(body)
msg.attach(MIMEText(contenido, 'html'))

# representa una conexion de un servidor de correo saliente (SMTP server)
server = smtplib.SMTP('smtp.gmail.com', 587)
# conexion segura
server.starttls()
# login
server.login(remitente, os.getenv('PASSWORD'))
# Enviar el correo
server.sendmail(remitente, destinatario, msg.as_string())
# cerrar la conexión
server.quit()