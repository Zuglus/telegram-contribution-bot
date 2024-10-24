# models/contribution.py
from sqlalchemy import Column, Integer, Float, String, DateTime, ForeignKey
from database.base import Base
import datetime

class Contribution(Base):
    __tablename__ = 'contributions'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)
    payment_date = Column(DateTime, nullable=False)
    full_name = Column(String, nullable=False)
    amount = Column(Float, nullable=False)
    month = Column(String, nullable=False)  # За какой месяц взнос
    note = Column(String, nullable=True)    # Примечание