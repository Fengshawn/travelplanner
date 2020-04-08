"""
@author:ZRM
@file:EmailSend.py
@time:2020/03/29
"""
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_email(toAddr):
    fromAddr = 'zrmzack@gmail.com'
    mypass = '123dreamture'
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
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromAddr, mypass)
    server.send_message(msg)

    server.quit()

#
# if __name__ == "__main__":
#     send_email('rzhang64@sheffield.ac.uk')
