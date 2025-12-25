"""
Token API routes

These endpoints expose token functionality to clients.
They delegate logic to the token service.
"""
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.services.token_service import add_tokens, consume_tokens

router = APIRouter(prefix="/tokens", tags=["tokens"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/add/{user_id}/{amount}")
def add(user_id: str, amount: int, reason: str, db: Session = Depends(get_db)):
    try:
        return add_tokens(db, user_id, amount, reason)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/consume/{user_id}/{amount}")
def consume(user_id: str, amount: int, reason: str, db: Session = Depends(get_db)):
    try:
        return consume_tokens(db, user_id, amount, reason)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
