from sqlalchemy.orm import Session
from app.models.user import User
from app.models.token_ledger import TokenLedger
import uuid

def add_tokens(db: Session, user_id: str, amount: int, reason: str):
    user = db.get(User, user_id)
    if not user:
        raise ValueError("User not found")
    user.tokens += amount
    ledger_entry = TokenLedger(
        id=str(uuid.uuid4()),
        user_id=user_id,
        change=amount,
        reason=reason
    )
    db.add(ledger_entry)
    db.commit()
    db.refresh(user)
    return user

def consume_tokens(db: Session, user_id: str, amount: int, reason: str):
    user = db.get(User, user_id)
    if not user:
        raise ValueError("User not found")
    if user.tokens < amount:
        raise ValueError("Not enough tokens")
    user.tokens -= amount
    ledger_entry = TokenLedger(
        id=str(uuid.uuid4()),
        user_id=user_id,
        change=-amount,
        reason=reason
    )
    db.add(ledger_entry)
    db.commit()
    db.refresh(user)
    return user
