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

def send_email(hack_name, name, id_from, id_to, link):
    subject_to_send = f"Certificate of Participation for the event {hack_name}"
    body = f"Congratulations {name},\nPlease find your certificates attached."
    message = Mail(
        from_email=id_from, to_emails=id_to, subject=subject_to_send, html_content=body
    )
    file = base64.b64encode(open("./certificate.pdf", "rb").read()).decode()

    attachedFile = Attachment(
        FileContent(file),
        FileName("Certificate.pdf"),
        FileType("application/pdf"),
        Disposition("attachment"),
    )
    message.attachment = attachedFile

    sg = SendGridAPIClient(
        api_key=(
            "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"
        )
    )
    response = sg.send(message)
    print(response.status_code, response.body, response.headers)
