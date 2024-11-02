import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from src.services.users.templates.html_show_message import send_template_change_password

from src.config import SENDER_EMAIL, SENDER_PASSWORD, SMTP_SERVER, SMTP_PORT


def send_verification_email(email: str, code: str):
    if not SENDER_EMAIL or not SENDER_PASSWORD or not SMTP_SERVER or not SMTP_PORT:
        raise Exception("Configurações de e-mail não encontradas")

    sender_email = SENDER_EMAIL
    sender_password = SENDER_PASSWORD
    smtp_server = SMTP_SERVER
    smtp_port = SMTP_PORT

    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = email
    message["Subject"] = "Código de Verificação para Redefinição de Senha"
    body = send_template_change_password(code)
    message.attach(MIMEText(body, "html"))

    with smtplib.SMTP(smtp_server, int(smtp_port)) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, email, message.as_string())
