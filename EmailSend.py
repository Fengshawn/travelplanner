"""

@author:ZRM&Areej
@file:EmailSend.py
@time:2020/03/29
"""
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText


def send_email(toAddr):
    """
    Send the PDF plan to the user's email address
    :param toAddr: email address to send the plan to
    :return:
    """
    fromAddr = 'travel.planner2030@gmail.com'   # Gmail Account
    mypass = 'Sh12345678'  # Gmail Account Password
    msg = MIMEMultipart()
    msg['From'] = fromAddr
    msg['to'] = toAddr
    msg['Subject'] = 'Travel Planner'
    body = '''
    The PDF for the travel plan is attached to this email
    '''
    # Start Areej Part
    msg.attach(MIMEText(body, 'plain'))
    with open('static/temp/plan.pdf', "rb") as f:
        attach = MIMEApplication(f.read(), _subtype="pdf")  # Attach the PDF to the email
    attach.add_header('Content-Disposition', 'attachment', filename=str('plan.pdf'))
    msg.attach(attach)
    # End Areej Part
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromAddr, mypass)  # Login with account
    server.send_message(msg)        # Send the email
    server.quit()                   # Quit server once done

