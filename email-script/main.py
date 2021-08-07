from config import api_key as key
import os
import base64
from urllib.request import Request, urlopen
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import (Mail, Attachment, FileContent, FileName, FileType, Disposition)
new_line='\n'

def email_send(hack_name,name,id_from,id_to,link):
    subject_to_send = f"MLH Certificate of Participation for the event {hack_name}"
    body = f"Congratulations {name},\nPlease find your certificates attached."
    message = Mail(
    from_email=id_from,
    to_emails=id_to,
    subject=subject_to_send,
    html_content=body
    )

    req = Request(link, headers = {'User-Agent':'Mozilla/5.0'})
    webpage = urlopen(req).read()
    encoded_file = base64.b64encode(webpage).decode()

    attachedFile = Attachment(
        FileContent(encoded_file),
        FileName('Certificate.pdf'),
        FileType('application/pdf'),
        Disposition('attachment')
    )
    message.attachment = attachedFile

    sg = SendGridAPIClient(api_key= key)
    response = sg.send(message)
    print(response.status_code, response.body, response.headers)
details = {'person1':{'name':'San','mail':'santhoshiravi1999@gmail.com','link':'http://skrn.ml/resume.pdf'},'person2':{'name':'Santho','mail':'san.athena29@gmail.com','link':'http://skrn.ml/resume.pdf'},'person3':{'name':'Karan','mail':'sreekaran.srinath@gmail.com','link':'http://skrn.ml/resume.pdf'}}  
hack_name='Robohacks'
id_from = 'santhoshiravi1999@gmail.com'
for detail in details:
    name = details[detail]['name']
    id_to = details[detail]['mail']
    links= details[detail]['link']
    email_send(hack_name,name,id_from,id_to,links)
    #     print(hack_name,name,id_to,id_from,links)