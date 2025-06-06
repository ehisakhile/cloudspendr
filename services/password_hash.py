from passlib.context import CryptContext

# Password hashing context
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# --- Utility Functions for Hashing Passwords ---
def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)