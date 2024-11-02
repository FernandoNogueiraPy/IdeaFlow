from fastapi import APIRouter

from src.routers.request_password_reset import request_password_router
from src.routers.verify_code import verify_code_router


full_routers = APIRouter()

full_routers.include_router(request_password_router)
full_routers.include_router(verify_code_router)
