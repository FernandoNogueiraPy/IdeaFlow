from pydantic import BaseModel, EmailStr


class LoginUser(BaseModel):
    id_user: str
    username: str
    password: str
    email: EmailStr
    full_name: str
