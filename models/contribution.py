from sqlalchemy import Column, Integer, Float, String, DateTime
from database.base import Base
import datetime

class Contribution(Base):
    __tablename__ = 'contributions'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False)
    amount = Column(Float, nullable=False)
    date = Column(DateTime, default=datetime.datetime.utcnow)
    description = Column(String, nullable=True)
