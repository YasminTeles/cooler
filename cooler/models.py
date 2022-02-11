from sqlalchemy import Column, Integer, String

from .database import Base


class History(Base):
    __tablename__ = 'history'

    id = Column(Integer, primary_key=True)
    type_beverage = Column(String, nullable=False)
    amount = Column(Integer, nullable=False)
    movement = Column(String, nullable=False)
