# db_models.py
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship


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
