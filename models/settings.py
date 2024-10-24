from sqlalchemy import Column, Integer, Boolean, String
from database.base import Base

class BotSettings(Base):
    __tablename__ = 'bot_settings'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    value = Column(Boolean, nullable=False)