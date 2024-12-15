from fastapi import FastAPI
from routes.email_routes import email_routes

app = FastAPI()
app.title = "Send email's app📧"
app.description = "This is a simple app for send email's from python using fastapi✉️"
app.version = "1.0.0"

app.include_router(email_routes, prefix='/email')