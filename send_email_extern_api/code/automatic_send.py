import smtplib
import os
from dotenv import load_dotenv
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Cargar variables de entorno
load_dotenv()

remitente = os.getenv('USER')
asunto = "Asunto del correo"

# Lista de destinatarios
destinatarios = ['correo1@example.com', 'correo2@example.com', 'correo3@example.com']

# Configurar el servidor SMTP
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(remitente, os.getenv('PASSWORD'))

for destinatario in destinatarios:
    # Crear el mensaje
    msg = MIMEMultipart()
    msg['From'] = remitente
    msg['To'] = destinatario
    msg['Subject'] = asunto

    # Cuerpo del mensaje
    cuerpo = f"Hola, este es un mensaje para {destinatario}."
    msg.attach(MIMEText(cuerpo, 'plain'))

    # Enviar el correo
    server.sendmail(remitente, destinatario, msg.as_string())
    print(f'Correo enviado a {destinatario}')

# Cerrar la conexión
server.quit()