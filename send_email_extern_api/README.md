<p align="center">
    <img src="https://upload.wikimedia.org/wikipedia/commons/0/0a/Python.svg" height="96">
    <img src="https://www.pngplay.com/wp-content/uploads/6/Red-Email-PNG-Clipart-Background.png" height="96">
    <h3 align="center">Send Email whith Python - Documentation</h3>
</p>

<p align="center">Es una aplicación simple en FastAPI desarrolada en un video tutorial de YouTube. <a href="https://www.youtube.com/watch?v=XLD2lqZj27Q&ab_channel=Pildorasdeprogramaci%C3%B3n">YouTube Video Tutorial</a></p>
<p> <a href="https://fastapi.tiangolo.com/">FastAPI</a> as the API backend.</p>

---

# Send Emails with Python

Para enviar correos electrónicos con Python, se utiliza la biblioteca `smtplib` para manejar el servidor SMTP y `email.mime` para construir el contenido del correo. Aquí te muestro cómo hacerlo:

<p>Lista de comandos para inciiar el proyecto: </p>
<ul>
    <li>pip install -r requirements.txt</li>
    <li>pip install python-dotenv</li>
    <li>uvicorn main:app --reload</li>
</ul>


### Pasos para enviar un correo

1. **Configura las variables de entorno:**
   - Crea un archivo `.env` para guardar tus credenciales (usuario y contraseña del correo) de manera segura.

2. **Prepara el contenido del correo:**
   - Utiliza `email.mime` para construir el cuerpo y el asunto del mensaje. Puedes adjuntar contenido HTML o texto plano.

3. **Conéctate al servidor SMTP:**
   - Configura el servidor SMTP (por ejemplo, `smtp.gmail.com` para Gmail) y realiza el inicio de sesión.

4. **Envía el correo:**
   - Usa `server.sendmail(remitente, destinatario, msg.as_string())`.

### Ejemplo básico

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
destinatario = os.getenv('YURE')
asunto = "Mensaje extenso de prueba"
```

# Crear el mensaje

```
msg = MIMEMultipart()
msg['From'] = remitente
msg['To'] = destinatario
msg['Subject'] = asunto
```

# Leer contenido HTML desde un archivo

```
with open('templates/airpods.html', 'r', encoding='utf-8') as archivo:
    contenido = archivo.read()

msg.attach(MIMEText(contenido, 'html'))
```

# Configurar servidor SMTP

```
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(remitente, os.getenv('PASSWORD'))
```

# Enviar correo

```
server.sendmail(remitente, destinatario, msg.as_string())
server.quit()
```
By: [Alexi Dg](www.linkedin.com/in/alexi-duran-gomez-6b17042a3)