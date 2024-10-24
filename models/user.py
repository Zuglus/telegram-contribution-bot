from sqlalchemy import Column, Integer, String, Boolean
from database.base import Base

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    telegram_id = Column(Integer, unique=True, nullable=False)
    full_name = Column(String, nullable=False)
    is_approved = Column(Boolean, default=False)
    is_admin = Column(Boolean, default=False)