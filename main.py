import datetime
import json
from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
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
    rate: float
    start_date: datetime.date


session = Session(bind=engine)


def calc_amortization_amt(principal, rate, term):
    i = (1 + rate) ** term
    return principal * rate * i / (i-1)


def amortization_sched(principal, rate, term):
    amortization = calc_amortization_amt(principal, rate, term)
    p = 1
    balance = principal
    while p <= term:
        interest = balance * rate
        principal = amortization - interest
        balance = balance - principal
        yield p, amortization, interest, principal, balance if balance > 0 else 0
        p += 1


@app.get('/')
async def root():
    return {'message': 'Hello World'}


@app.post(f'/{MAJOR}/user/')
async def create_user(user: User):
    new_user = User_Table(email=user.email, first=user.first_name,
                          last=user.last_name, phone=user.phone)
    session.add(new_user)
    session.commit()
    return user


@app.post(f'/{MAJOR}/loan/')
async def create_loan(loan: Loan):
    new_loan = Loan_Table(user_id=loan.userid, principal=loan.principal_amount,
                          term=loan.term, interest=loan.rate, start_date=loan.start_date)
    session.add(new_loan)
    session.commit()
    return loan


@app.get(f'/{MAJOR}/loan/schedule')
async def get_loan_schedule(loan_id):
    loan = session.query(Loan_Table).get(loan_id)
    sched = amortization_sched(loan.principal, loan.rate, loan.term)
    return json.dumps(sched)


@app.get(f'/{MAJOR}/loan/month')
async def get_loan_summary(loan_id, month):
    loan = session.query(Loan_Table).get(loan_id)
    sched = amortization_sched(loan.principal, loan.rate, month)
    return sched


@app.get(f'/{MAJOR}/user/loans')
async def get_all_user_loans(user_id):
    loans = session.query(Loan_Table).get(user_id)
    return jsonable_encoder(loans)


@app.get(f'/{MAJOR}/user/shareloan')
async def share_loan(user_id, loan_id):
    return user_id, loan_id
