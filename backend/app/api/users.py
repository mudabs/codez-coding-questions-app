from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.deps import get_db
from app.schemas.user import UserCreate, UserResponse
from app.crud.user import create_user, get_user_by_email
from app.api.deps import get_current_user
from app.models.user import User
from fastapi import Depends

router = APIRouter(prefix="/users", tags=["users"])

@router.post("/", response_model=UserResponse)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    existing = get_user_by_email(db, user.email)
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")

    return create_user(db, user)

@router.get("/me")
def read_current_user(current_user: User = Depends(get_current_user)):
    """
    Return the currently authenticated user.

    This endpoint is protected:
    - Requires Authorization: Bearer <token>
    """
    return current_user
