import os
import base64
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import (
    Mail,
    Attachment,
    FileContent,
    FileName,
    FileType,
    Disposition,
)

import setupenv


def send_email(hack_name, name, from_email, to_emails, link):
    subjec = f"Certificate of Participation for the event {hack_name}"
    body = f"Congratulations {name},\nPlease find your certificates attached."
    message = Mail(
        from_email=from_email, to_emails=to_emails, subject=subjec, html_content=body
    )
    file = base64.b64encode(open("./certificate.pdf", "rb").read()).decode()

    attachedFile = Attachment(
        FileContent(file),
        FileName("certificate.pdf"),
        FileType("application/pdf"),
        Disposition("attachment"),
    )
    message.attachment = attachedFile

    sg = SendGridAPIClient(api_key=os.getenv("SENDGRID_API_KEY"))
    response = sg.send(message)
    print(response.status_code, response.body, response.headers)
