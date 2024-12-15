import smtplib
import os
from dotenv import load_dotenv
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.message import MIMEMessage

# Upload eviroments variables from .env archive
load_dotenv()

remitente = os.getenv('USER')
destinatario = os.getenv('ALEXI')
asunto = "Mensaje extenso de prueba"

msg = MIMEMultipart()
msg['From'] = remitente
msg['To'] = destinatario
msg['Subject'] = asunto

base_dir = os.path.dirname(os.path.realpath(__file__))
file = os.path.join(base_dir, 'templates/airpods.html')

with open(file, 'r', encoding='utf-8') as archive:
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