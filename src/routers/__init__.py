from fastapi import APIRouter

from src.routers.users.auth_user import router_auth_user
from src.routers.users.register_user import router_register_user
from src.routers.users.request_password_reset import request_password_router
from src.routers.users.verify_code import verify_code_router
from src.routers.users.changed_password import router_changed_password


full_routers = APIRouter()


full_routers.include_router(router_auth_user)
full_routers.include_router(router_register_user)
full_routers.include_router(request_password_router)
full_routers.include_router(verify_code_router)
full_routers.include_router(router_changed_password)
