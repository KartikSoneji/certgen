"""
Certificate Generator API -
When given a name and email address, this module will plug values into a certificate template and upload it to an astradb instance, and also call the email script to email the certificates to the given emails.
"""

import os
from flask import Flask
import requests
import flask
import psycopg2
from flask import request
from mailer import send_email

import setupenv

CERTIFICATE_TEMPLATE = """
<html>
    <head>
        <style type="text/css">
            body,
            html {
                margin: 0;
                padding: 0;
            }
            body {
                color: black;
                display: table;
                font-family: Georgia, serif;
                font-size: 24px;
                text-align: center;
            }
            .container {
                border: 20px solid tan;
                width: 750px;
                height: 563px;
                display: table-cell;
                vertical-align: middle;
            }
            .logo {
                color: tan;
            }
            .marquee {
                color: tan;
                font-size: 48px;
                margin: 20px;
            }
            .assignment {
                margin: 20px;
            }
            .person {
                border-bottom: 2px solid black;
                font-size: 32px;
                font-style: italic;
                margin: 20px auto;
                width: 400px;
            }
            .reason {
                margin: 20px;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <div class="logo">An Organization</div>
            <div class="marquee">Certificate of Completion</div>
            <div class="assignment">This certificate is presented to</div>
            <div class="person">%s</div>
            <div class="reason">
                For deftly defying the laws of gravity<br />
                and flying high
            </div>
        </div>
    </body>
</html>
"""

app = Flask(__name__)
conn = psycopg2.connect(os.environ.get("COCKROACH_DSN"))


@app.route("/")
def generateCertificates():
    name = request.args.get("name")
    email = request.args.get("email")

    generate_certificate_cached_cockroachdb(name, email)
    send_email(
        "RoboHacks", name, "sreekaransrinath@gmail.com", email, "certificate.pdf"
    )
    status_code = flask.Response(status=200)
    return "Generated"

def generate_certificate_cached_cockroachdb(name, email):
    with conn.cursor() as cur:
        cur.execute("SELECT certificate FROM Certificates WHERE name = %s AND email = %s", (name, email))
        row = cur.fetchone()
        if row:
            open("certificate.pdf", "wb").write(row[0])
            return

    certTemplate = CERTIFICATE_TEMPLATE % name
    response = requests.post(
        "http://api.pdflayer.com/api/convert",
        params={"access_key": os.getenv("PDFLAVER_API_KEY")},
        data={"document_html": certTemplate, "test": 1},
    )
    open("certificate.pdf", "wb").write(response.content)
    with conn.cursor() as cur:
        cur.execute(
          "UPSERT INTO Certificates (name, email, certificate) VALUES (%s, %s, %s)",
          (name, email, psycopg2.Binary(response.content))
        )
    conn.commit()

def setup_database():
	with conn.cursor() as cur:
		cur.execute("CREATE DATABASE IF NOT EXISTS HackCal")
		cur.execute("USE HackCal")

		cur.execute("""
			CREATE TABLE IF NOT EXISTS Certificates (
				name STRING,
				email STRING,
				certificate BLOB
			)
		""")
	conn.commit()

if __name__ == "__main__":
    setup_database()
    app.run()
