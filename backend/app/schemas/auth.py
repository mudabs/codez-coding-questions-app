"""
auth.py

Pydantic models for authentication-related requests and responses.
These models define the API contract for login.
"""

from pydantic import BaseModel, EmailStr


class LoginRequest(BaseModel):
    """
    Data required to log in.

    For now, we only authenticate by email.
    Passwords will be added later.
    """
    email: EmailStr


class TokenResponse(BaseModel):
    """
    Response returned after successful login.
    """
    access_token: str
    token_type: str = "bearer"
