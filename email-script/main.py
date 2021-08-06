import base64

from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import (Mail, Attachment, FileContent, FileName, FileType, Disposition)


message = Mail(
    from_email='santhoshiravi1999@gmail.com',
    to_emails='santhoshiravi1999@gmail.com',
    subject='Sending with Twilio SendGrid is Fun',
    html_content='<strong>and easy to do anywhere, even with Python</strong>'
)

with open('F:/Final year project/IRJET.pdf', 'rb') as f:
    data = f.read()
    f.close()
encoded_file = base64.b64encode(data).decode()

attachedFile = Attachment(
    FileContent(encoded_file),
    FileName('attachment.pdf'),
    FileType('application/pdf'),
    Disposition('attachment')
)
message.attachment = attachedFile

sg = SendGridAPIClient(api_key=('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'))
response = sg.send(message)
print(response.status_code, response.body, response.headers)
