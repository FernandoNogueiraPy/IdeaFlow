import random
import string
from datetime import datetime, timedelta


verification_codes_permission: dict[str, dict[str, str | datetime | bool]] = {}


def generate_verification_code():
    return "".join(random.choices(string.ascii_uppercase + string.digits, k=6))


def store_verification_code(email: str, code: str):
    expiration_time = datetime.utcnow() + timedelta(
        minutes=10
    )  # Código expira em 10 minutos
    verification_codes_permission[email] = {
        "code": code,
        "expires_at": expiration_time,
        "change_password": False,
    }
