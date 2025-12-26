"""
security.py

This file contains all authentication-related helpers.
Nothing here talks to FastAPI directly — it only handles JWT logic.

Keeping this separate makes the code:
- easier to test
- easier to reason about
- reusable across routes
"""

from datetime import datetime, timedelta, timezone
from jose import jwt
import os
from jose import JWTError


# These values come from .env
# They define how tokens are signed and how long they live
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM", "HS256")
ACCESS_TOKEN_EXPIRE_MINUTES = int(
    os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 60)
)


def create_access_token(data: dict) -> str:
    """
    Create a signed JWT token.

    Parameters:
    - data: dictionary that will become the JWT payload.
      Example: {"sub": user_id, "email": user.email}

    Returns:
    - A JWT token string
    """

    # Copy the data so we don't mutate the original dict
    to_encode = data.copy()

    # Calculate expiration time
    expire = datetime.now(timezone.utc) + timedelta(
        minutes=ACCESS_TOKEN_EXPIRE_MINUTES
    )

    # Add expiration claim to payload
    to_encode.update({"exp": expire})

    # Create and sign the JWT
    encoded_jwt = jwt.encode(
        to_encode,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

    return encoded_jwt

def decode_access_token(token: str) -> dict:
    """
    Decode and validate a JWT token.

    Parameters:
    - token: JWT string from Authorization header

    Returns:
    - decoded payload (dict)

    Raises:
    - JWTError if token is invalid or expired
    """

    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )
        return payload
    except JWTError:
        # Any problem with the token ends up here:
        # - expired
        # - wrong signature
        # - malformed
        raise