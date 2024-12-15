<p align="center"> 
    <img src="https://upload.wikimedia.org/wikipedia/commons/0/0a/Python.svg" height="96"> 
    <img src="https://www.pngplay.com/wp-content/uploads/6/Red-Email-PNG-Clipart-Background.png" height="96">
    <h3 align="center">Send Email with Python - Documentation</h3>
</p>

<p align="center">Es una aplicación simple en Python con funcionalidades extendidas con FastAPI. Desarrollada en un video tutorial de YouTube. <a href="https://www.youtube.com/watch?v=XLD2lqZj27Q&ab_channel=Pildorasdeprogramaci%C3%B3n">YouTube Video Tutorial</a></p>
<p> <a href="https://fastapi.tiangolo.com/">FastAPI</a> as the API backend.</p>

---

# Send Emails with Python

Para enviar correos electrónicos con Python, se utiliza la biblioteca `smtplib` para manejar el servidor SMTP y `email.mime` para construir el contenido del correo. Aquí te muestro cómo hacerlo:

### Pasos para enviar un correo:

1. **Configura las variables de entorno:**
   - Crea un archivo `.env` para guardar tus credenciales (usuario y contraseña del correo) de manera segura.

2. **Prepara el contenido del correo:**
   - Utiliza `email.mime` para construir el cuerpo y el asunto del mensaje. Puedes adjuntar contenido HTML o texto plano.

3. **Conéctate al servidor SMTP:**
   - Configura el servidor SMTP (por ejemplo, `smtp.gmail.com` para Gmail) y realiza el inicio de sesión.

4. **Envía el correo:**
   - Usa `server.sendmail(remitente, destinatario, msg.as_string())`.

### Ejemplo básico:

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

---

# Automatización del envío de correos

Puedes automatizar el envío de correos electrónicos a múltiples destinatarios o configurar tareas recurrentes. A continuación, se explica cómo hacerlo:

### Pasos para enviar correos a múltiples destinatarios

1. **Crea una lista de destinatarios:**
   - Puedes almacenarlos en un archivo CSV, una base de datos, o directamente en una lista de Python.

2. **Itera sobre los destinatarios:**
   - Utiliza un bucle para enviar el correo a cada destinatario.

3. **Agrega una conexión con una base de datos (opcional):**
   - Usa bibliotecas como `SQLAlchemy` o `sqlite3` para obtener datos directamente de una base de datos.

### Ejemplo para múltiples destinatarios

```python
destinatarios = ['correo1@example.com', 'correo2@example.com', 'correo3@example.com']

# Configurar servidor SMTP
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

server.quit()
```

---

# Consideraciones adicionales

- **Seguridad:** Asegúrate de que tus credenciales estén seguras utilizando variables de entorno con `dotenv`.
- **Manejo de errores:** Implementa excepciones para manejar errores comunes, como fallos en la conexión o destinatarios no válidos.
- **Automatización:** Usa tareas programadas (como cron jobs en Linux o el Programador de Tareas en Windows) para ejecutar el script periódicamente.
- **Conexión a una base de datos:** Puedes almacenar y recuperar destinatarios desde una base de datos relacional como MySQL o PostgreSQL.

### Automatización avanzada

Puedes combinar el script con un sistema de backend como FastAPI para que los correos se envíen automáticamente en respuesta a solicitudes o eventos específicos.

---

By: [Alexi Dg](www.linkedin.com/in/alexi-duran-gomez-6b17042a3)
