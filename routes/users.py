from fastapi import APIRouter
from schemas.users import UserTodo


router = APIRouter(prefix="/users", tags = ["users"])

# Todo - Create User Endpoint - Sophia & Ekon

@router.get("/todo", response_model=UserTodo)
def todo_users():
    return{"todo": "API to be implemented by Sophia & Ekon"}
