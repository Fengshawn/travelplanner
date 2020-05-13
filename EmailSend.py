"""
@author:ZRM
@file:EmailSend.py
@time:2020/03/29
"""
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText


def send_email(toAddr):
    fromAddr = 'travel.planner2030@gmail.com'
    mypass = 'Sh12345678'
    msg = MIMEMultipart()
    msg['From'] = fromAddr
    msg['to'] = toAddr
    msg['Subject'] = 'Travel Planner'
    body = '''
    #this is flight inforamtion

    #this is hotel informaiton

    #this is attractions infroamtion

    '''
    msg.attach(MIMEText(body, 'plain'))
    with open('static/temp/plan.pdf', "rb") as f:
        # attach = email.mime.application.MIMEApplication(f.read(),_subtype="pdf")
        attach = MIMEApplication(f.read(), _subtype="pdf")
    attach.add_header('Content-Disposition', 'attachment', filename=str('static/temp/plan.pdf'))
    msg.attach(attach)
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromAddr, mypass)
    server.send_message(msg)

    server.quit()

#
if __name__ == "__main__":
    send_email('travel.planner2030@gmail.com')
