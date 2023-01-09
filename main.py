from fastapi import FastAPI
from pydantic import BaseModel

from db_models import Session
from db_models import Loan_Table
from db_models import User_Table
from db_models import engine


app = FastAPI()
MAJOR = 'v1'


class User(BaseModel):
    first_name: str
    last_name: str
    email: str
    phone: str | None = None


class Loan(BaseModel):
    userid: int
    principal_amount: float
    term: int
    apr: float


session = Session(bind=engine)


@app.get('/')
async def root():
    return {'message': 'Hello World'}


@app.post(f'/{MAJOR}/user/')
async def create_user(user: User):
    new_user = User_Table(email='', first='', last='', phone='')
    session.add(new_user)
    session.commit()
    return user


@app.post(f'/{MAJOR}/loan/')
async def create_loan(loan: Loan):
    new_loan = Loan_Table(user_id='', principal='',
                          term='', interest='', start_date='')
    session.add(new_loan)
    session.commit()
    return loan


@app.get(f'/{MAJOR}/loan/schedule')
async def get_loan_schedule(loan_id):
    return loan_id


@app.get(f'/{MAJOR}/loan/month')
async def get_loan_summary(month):
    return month


@app.get(f'/{MAJOR}/user/loans')
async def get_all_user_loans(user_id):
    session.query(Loan_Table).get(user_id)
    return user_id


@app.get(f'/{MAJOR}/user/shareloan')
async def share_loan(user_id, loan_id):
    return user_id, loan_id
