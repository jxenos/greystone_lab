# db_models.py
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Float
from sqlalchemy import Date
from sqlalchemy import DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class User_Table(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    # in a real env recommend having a guid as well
    first_name = Column(String(30))
    last_name = Column(String(30))
    email = Column(String(50))
    phone = Column(Integer(10))

    def __repr__(self):
        return f"User_Table(id={self.id!r}, first={self.first_name!r}, last={self.last_name!r})"


class Loan_Table(Base):
    __tablename__ = "loan"

    id = Column(Integer, primary_key=True)
    # guid
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    principal = Column(Float)
    term = Column(Integer(3))
    apr = Column(Float)
    start_date = Column(Date)
    created_date = Column(DateTime(timezone=False), server_default=func.now())

    def __repr__(self):
        return f"Loan_Table(id={self.id!r}, principal={self.principal!r}, term={self.term!r}, apr={self.apr!r})"
