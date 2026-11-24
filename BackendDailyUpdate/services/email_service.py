import os
import smtplib

from email.message import EmailMessage
from dotenv import load_dotenv

load_dotenv()


def send_task_email(task_title: str):
    try:
        print("Background email function started")

        message = EmailMessage()
        message["Subject"] = "New Task Created"
        message["From"] = os.getenv("EMAIL_ADDRESS")
        message["To"] = os.getenv("NOTIFICATION_EMAIL")

        message.set_content(
            f"Your new task has been created: {task_title}"
        )

        with smtplib.SMTP_SSL(
            "smtp.gmail.com", 465
        ) as server:

            print("SMTP connected")

            server.login(
                os.getenv("EMAIL_ADDRESS"),
                os.getenv("EMAIL_PASSWORD")
            )

            print("Gmail login successful")

            server.send_message(message)

        print("Email sent successfully")

    except Exception as e:
        print("EMAIL ERROR:", repr(e))