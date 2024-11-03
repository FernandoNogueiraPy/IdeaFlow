from dotenv import load_dotenv
from os import getenv


load_dotenv()

URL_MONGO = getenv("URL_MONGO")
DATABASE = getenv("DATABASE")
COLLECTION_USERS = getenv("COLLECTION_USERS")


SECRET_KEY = getenv("SECRET_KEY")
ALGORITHM = getenv("ALGORITHM")

SENDER_EMAIL = getenv("SENDER_EMAIL")
SENDER_PASSWORD = getenv("SENDER_PASSWORD")
SMTP_SERVER = getenv("SMTP_SERVER")
SMTP_PORT = getenv("SMTP_PORT")
