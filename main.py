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


@app.post(f'/{MAJOR}/loan/')
async def create_loan(loan: User):
    return loan


@app.get(f'/{MAJOR}/loan/schedule')
async def get_loan_schedule(loanid):
    return loanid


@app.get(f'/{MAJOR}/loan/month')
async def get_loan_summary(month, year):
    return month, year


@app.get(f'/{MAJOR}/user/loans')
async def get_all_user_loans(userid):
    return userid


@app.get(f'/{MAJOR}/user/shareloan')
async def share_loan(userid, loanid):
    return userid, loanid
