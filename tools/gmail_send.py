"""
@author:ZRM
@file:gmail_send.py
@time:2020/03/29
"""
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

fromAddr = 'zrmzack@gmail.com'
mypass = '123dreamture'
toAddr = 'rzhang64@sheffield.ac.uk'
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
server.login('zrmzack@gmail.com', '123dreamture')
server.send_message(msg)
server.quit()

if __name__ == "__main__":
    pass
