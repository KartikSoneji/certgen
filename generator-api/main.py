"""
Certificate Generator API -
When given a name and email address, this module will plug values into a certificate template and upload it to an astradb instance, and also call the email script to email the certificates to the given emails.
"""

from flask import Flask
import requests
from weasyprint import HTML

app = Flask(__name__)


def uploadtoAstraDB(name, email, certificate):
    pass


@app.route("/")
def generateCertificates(name, email):
    certTemplate = (
        """<html> <head> <style type='text/css'> body, html{margin: 0; padding: 0;}body{color: black; display: table; font-family: Georgia, serif; font-size: 24px; text-align: center;}.container{border: 20px solid tan; width: 750px; height: 563px; display: table-cell; vertical-align: middle;}.logo{color: tan;}.marquee{color: tan; font-size: 48px; margin: 20px;}.assignment{margin: 20px;}.person{border-bottom: 2px solid black; font-size: 32px; font-style: italic; margin: 20px auto; width: 400px;}.reason{margin: 20px;}</style> </head> <body> <div class="container"> <div class="logo"> An Organization </div><div class="marquee"> Certificate of Completion </div><div class="assignment"> This certificate is presented to </div><div class="person"> %s </div><div class="reason"> For deftly defying the laws of gravity<br/> and flying high </div></div></body></html>"""
        % name
    )
    # uploadtoAstraDB(name, email)
    response = requests.post(
        "http://api.pdflayer.com/api/convert",
        params={"access_key": "20e0e411fe097670f57c890ce1650932"},
        data={"document_html": certTemplate},
    )
    open("cert.pdf", "wb").write(response.content)

if __name__ == "__main__":
    app.run()
