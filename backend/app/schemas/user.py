from pydantic import BaseModel, EmailStr
from datetime import datetime

class UserCreate(BaseModel):
    email: EmailStr
    phone: str | None = None

class UserResponse(BaseModel):
    id: int
    email: EmailStr
    phone: str | None
    tokens: int
    created_at: datetime

    class Config:
        from_attributes = True
