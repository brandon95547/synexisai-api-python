import os
from email.message import EmailMessage
from aiosmtplib import send
from dotenv import load_dotenv

# Load credentials from .env
load_dotenv()

SMTP_HOST = os.getenv("SMTP_HOST")
SMTP_PORT = int(os.getenv("SMTP_PORT"))
SMTP_USER = os.getenv("SMTP_USER")
SMTP_PASS = os.getenv("SMTP_PASS")
DEFAULT_FROM = os.getenv("DEFAULT_FROM", SMTP_USER)

async def send_email(data):
    to_address = data.get("to")
    subject = data.get("subject", "No Subject")
    message_body = data.get("message", "")

    if not to_address or not message_body:
        return "Missing 'to' or 'message'"

    msg = EmailMessage()
    msg["From"] = DEFAULT_FROM
    msg["To"] = to_address
    msg["Subject"] = subject
    msg.set_content(message_body)

    try:
        await send(
            msg,
            hostname=SMTP_HOST,
            port=SMTP_PORT,
            username=SMTP_USER,
            password=SMTP_PASS,
            start_tls=True,
        )
        return "Email sent"
    except Exception as e:
        return f"Failed to send email: {str(e)}"
