from fastapi import FastAPI
from app.db.session import engine
from app.db.base import Base
from app.api.users import router as users_router
from app.api import tokens 
from app.api.auth import router as auth_router


app = FastAPI(title="Codez")

Base.metadata.create_all(bind=engine)

app.include_router(users_router)
app.include_router(tokens.router)
app.include_router(auth_router)

@app.get("/health")
def health_check():
    return {"status": "OK"}
