from fastapi import APIRouter, Depends, HTTPException, status  ##SOPIA,MAGGIE&EKON
from sqlalchemy.orm import Session                      ##SOPIA,MAGGIE&EKON
from schemas.users import UserTodo, UserCreate, User             ##SOPIA,MAGGIE&EKON
from config.database import get_db                      ##SOPIA,MAGGIE&EKON
from models.users import User as UserModel                  ###SOPIA,MAGGIE&EKON
from services.password_hash import get_password_hash                 ###SOPIA,MAGGIE&EKON


router = APIRouter(prefix="/users", tags = ["users"])

# Todo - Create User Endpoint - Sophia & Ekon

@router.get("/todo", response_model=UserTodo)
def todo_users():
    return{"todo": "API to be implemented by Sophia & Ekon"}


###====================================================================================================
# API FOR CREATE USER WIC WILL INCLUDE, EMAIL, USER, NAME AND PASSWORD. TIS API WILL Validate the data, 
# Hash the password, Save the user to the MySQL RDS database AND Return a success message ##SOPIA,MAGGIE&EKON
##=======================================================================================================

router = APIRouter(prefix="/users", tags=["users"])

# POST /users - Create a new user
@router.post("/", response_model=User, status_code=status.HTTP_201_CREATED)
def create_user(user_data: UserCreate, db: Session = Depends(get_db)):
    # 1. Check if email or username already exists
    existing_user = db.query(UserModel).filter(
        (UserModel.email == user_data.email) | 
        (UserModel.username == user_data.username)
    ).first()

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Email or username already exists"
        )

    # 2. Hash the password
    hashed_password = get_password_hash(user_data.password)

    # 3. Create a new User object
    new_user = UserModel(
        email=user_data.email,
        username=user_data.username,
        hashed_password=hashed_password,
        first_name=None,
        last_name=None
    )

    # 4. Save to database
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user
