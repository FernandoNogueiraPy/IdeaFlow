from fastapi import APIRouter

from src.entities.users.response_auth import ReponseAuth
from src.entities.users.auth_user import AuthUser
from src.services.users.user_service import UserService

router_auth_user = APIRouter()


@router_auth_user.post("/auth", tags=["USERS"], response_model=ReponseAuth)
async def authenticate_user(auth_user: AuthUser) -> ReponseAuth:
    return UserService().authenticate_user(auth_user)