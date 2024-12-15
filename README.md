<p align="center">
    <img src="https://upload.wikimedia.org/wikipedia/commons/0/0a/Python.svg" height="96">
    <img src="https://www.pngplay.com/wp-content/uploads/6/Red-Email-PNG-Clipart-Background.png" height="96">
    <h3 align="center">Send Email whith Python - Documentation</h3>
</p>

<p align="center">Es una aplicación simple en FastAPI desarrolada en un video tutorial de YouTube. <a href="https://www.youtube.com/watch?v=XLD2lqZj27Q&ab_channel=Pildorasdeprogramaci%C3%B3n">YouTube Video Tutorial</a></p>
<p> <a href="https://fastapi.tiangolo.com/">FastAPI</a> as the API backend.</p>

# Send Emial's with python

Para automatizar el envío de correos electrónicos múltiples en Python, puedes seguir estos pasos:

Preparar el entorno: Asegúrate de tener Python instalado y las bibliotecas necesarias. Puedes usar smtplib para enviar correos y dotenv para manejar variables de entorno (como tus credenciales de correo).

Crear una lista de destinatarios: Puedes almacenar las direcciones de correo electrónico en una lista o leerlas desde un archivo (como un CSV).

Configurar el correo electrónico: Utiliza un bucle para iterar sobre la lista de destinatarios y enviar un correo a cada uno.

Ejemplo de código: Aquí tienes un ejemplo básico de cómo hacerlo:

```
import smtplib
import os
from dotenv import load_dotenv
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
```

# Cargar variables de entorno

```
load_dotenv()

remitente = os.getenv('USER')
asunto = "Asunto del correo"
```

# Lista de destinatarios

destinatarios = ['correo1@example.com', 'correo2@example.com', 'correo3@example.com']

# Configurar el servidor SMTP

```
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
```
# Cerrar la conexión

```
server.quit()
```
Consideraciones:

Asegúrate de que tu cuenta de correo permita el acceso a aplicaciones menos seguras si usas Gmail.
Considera implementar un manejo de errores para gestionar posibles fallos en el envío.
Si envías muchos correos, verifica las políticas de tu proveedor de correo para evitar ser marcado como spam.
Automatización: Puedes programar este script para que se ejecute automáticamente usando un cron job en Linux o el Programador de tareas en Windows.

Siguiendo estos pasos, podrás automatizar el envío de correos electrónicos a múltiples destinatarios de manera efectiva.
