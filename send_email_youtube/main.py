from fastapi import FastAPI

app = FastAPI()
app.title = "Send email's app📧"
app.description = "This is a simple app for send email's from python using fastapi✉️"
app.version = "1.0.0"

@app.get('/', tags=['home'])
async def read_root():
    return {"message": "Hello, World!"}