from pydantic import BaseModel


class ReponseAuth(BaseModel):
    user_id: str
    access_token: str
    token_type: str = "bearer"
    message: str
