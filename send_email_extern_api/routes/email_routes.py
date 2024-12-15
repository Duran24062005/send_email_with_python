from fastapi import APIRouter

email_routes = APIRouter()

@email_routes.get('/', tags=['email'])
def read_emails():
    return {"read": "email"}