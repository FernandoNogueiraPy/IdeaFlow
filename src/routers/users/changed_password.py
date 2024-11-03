from fastapi import APIRouter
from src.services.users.user_service import UserService

router_changed_password = APIRouter()


@router_changed_password.post("/change_password", tags=["USERS"])
async def change_password_user(email: str, new_password: str):
    return UserService().change_password(email, new_password)
