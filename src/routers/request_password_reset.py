from fastapi import APIRouter

from src.services.users.send_email_rescue import send_verification_email

from src.services.users.create_code_rescue import (
    generate_verification_code,
    store_verification_code,
)


request_password_router = APIRouter()


@request_password_router.post("/request-password-reset")
async def request_password_reset(email: str):
    code = generate_verification_code()
    store_verification_code(email, code)
    send_verification_email(email, code)
    return {"message": "Código de verificação enviado para o e-mail"}
