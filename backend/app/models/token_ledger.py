"""
TokenLedger model

This table stores a history of all token changes.
Each row represents a single event:
- tokens added (positive number)
- tokens consumed (negative number)

This allows auditing, debugging, and future features
like refunds or subscriptions.
"""

from sqlalchemy import Column, String, Integer, DateTime, ForeignKey, func
from app.db.base import Base

class TokenLedger(Base):
    __tablename__ = "token_ledger"

    id = Column(String, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    change = Column(Integer)  # +ve for credit, -ve for usage
    reason = Column(String)  # e.g., "purchase", "daily free", "usage"
    created_at = Column(DateTime(timezone=True), server_default=func.now())
