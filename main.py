from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
MAJOR = 'v1'


class User(BaseModel):
    first_name: str
    last_name: str
    email: str
    phone: str | None = None


@app.get('/')
async def root():
    return {'message': 'Hello World'}


@app.post(f'/{MAJOR}/user/')
async def create_user(user: User):
    return user
