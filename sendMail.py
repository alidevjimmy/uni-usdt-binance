import smtplib
import ssl
from dotenv import load_dotenv
from os.path import dirname, join
import os
import sys


def sendMail(msg):
    dotenv_path = join(dirname(__file__), '.env')
    load_dotenv(dotenv_path)

    email = os.environ.get('EMAIL')
    password = os.environ.get('PASSWORD')

    smtp_server = os.environ.get('SMTP_SERVER')
    port = os.environ.get('PORT')

    context = ssl.create_default_context()
    try:
        server = smtplib.SMTP(smtp_server, port)
        server.ehlo()
        server.starttls(context=context)
        server.ehlo()
        server.login(email, password)
        server.sendmail(email, email, msg)
    except Exception as e:
        print(e)
        sys.exit()
    finally:
        server.quit()
