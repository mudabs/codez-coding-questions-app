from sqlalchemy import Column, String, Integer, DateTime, func
from sqlalchemy.sql import func
from app.db.base import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key = True, index=True)
    email=Column(String, unique = True, index = True)
    phone = Column(String, unique=True, nullable=True)
    tokens = Column(Integer, default=5)
    created_at = Column(DateTime(timezone=True), server_default=func.now())


    