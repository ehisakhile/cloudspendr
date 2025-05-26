from fastapi import FastAPI
from passlib.context import CryptContext
import models
from database import SessionLocal, engine

app = FastAPI()
models.base.metadata.create_all(bind=engine)
database = SessionLocal()


# Password hashing context
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# --- Utility Functions for Hashing Passwords ---
def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

@app.on_event("startup")
async def startup_event():
    # Ensure database tables are created
    models.Base.metadata.create_all(bind=database.engine)
    print("Database tables ensured.")


@app.get("/")
def homepage():
    return {"status": "CloudSpendr Home"}

@app.get("/health")
def health_check():
    return {"status": "API is running"}
