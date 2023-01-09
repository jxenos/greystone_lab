# db_models.py
import os
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Float
from sqlalchemy import Date
from sqlalchemy import DateTime
from sqlalchemy import create_engine

from sqlalchemy.sql import func
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker

BASE_DIR = os.path.dirname(os.path.realpath(__file__))
connection_string = f"sqlite:///{os.path.join(BASE_DIR,'site.db')}"

Base = declarative_base()

engine = create_engine(connection_string, echo=True)

Session = sessionmaker()


class User_Table(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    # in a real env recommend having a guid as well
    first_name = Column(String(30))
    last_name = Column(String(30))
    email = Column(String(50))
    phone = Column(Integer())

    def __repr__(self):
        return f"User_Table(id={self.id!r}, first={self.first_name!r}, last={self.last_name!r})"


class Loan_Table(Base):
    __tablename__ = "loan"

    id = Column(Integer, primary_key=True)
    # guid
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    principal = Column(Float)
    term = Column(Integer())
    rate = Column(Float)
    start_date = Column(Date)
    created_date = Column(DateTime(timezone=True), server_default=func.now())

    def __repr__(self):
        return f"Loan_Table(id={self.id!r}, principal={self.principal!r}, term={self.term!r}, apr={self.apr!r})"


class Payment_Table(Base):
    __tablename__ = "payment"

    id = Column(Integer, primary_key=True)
    # guid
    loan_id = Column(Integer, ForeignKey("loan.id"), nullable=False)
    principal_paid = Column(Float)
    interest_paid = Column(Float)
    principal_remaining = Column(Float)

    def __repr__(self):
        return f"Payment_Table(id={self.id!r}, loan_id={self.loan_id!r}, principal_paid={self.principal_paid!r}, interest_paid={self.interest_paid!r}, principal_remaining={self.principal_remaining!r})"
